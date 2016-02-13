# reference (this is the enemy deployment from mission 1)
        #create_ship(Havoc(),(13,9))
        #create_ship(PirateDestroyer(),(13,7))
        #create_ship(PirateDestroyer(),(13,8))
        #create_ship(PirateDestroyer(),(13,10))
        #create_ship(PirateDestroyer(),(13,11))
        #create_ship(PirateIronhog(),(13,6))
        #create_ship(PirateIronhog(),(13,12))
        #create_ship(PirateGrunt(),(11,6))
        #create_ship(PirateGrunt(),(11,7))
        #create_ship(PirateGrunt(),(11,10))
        #create_ship(PirateGrunt(),(11,11))
        #create_ship(PirateBomber(),(11,12))
        #create_ship(PirateBomber(),(11,5))

init 10 python:
    from random import randint
    
    arcade = None
    
    def loadArcadeManager():
        if hasattr(store,'arcade'):
            arcade = store.arcade
        
        if arcade is None:
            arcade = {}
            arcade.currentWave = -1
            arcade.currentTurn = -1
            arcade.turnsSinceLastWave = 0
            arcade.newWaveThisTurn = False
            arcade.finalWave = False
            arcade.moneyEarned = 0
            arcade.moneySpent = 0
            arcade.shipsDestroyed = 0
            arcade.spawnedAllyShips = []
            
        #arcade.waves = arcadeWaveDefs
        arcade.showingStore = False
        arcade.storeItems = arcadeStoreItems
        store.arcade = arcade
    
    def getArcadeMoneyEarned():
        if len(destroyed_ships) == arcade.shipsDestroyed:
            return arcade.moneyEarned - arcade.moneySpent
            
        # recalculate money
        money = 0
        for ship in destroyed_ships:
            if ship.faction != 'Player':
                money += ship.money_reward
                
        if store.Difficulty == 5:       # space whale tax
            money *= 0.8
        
        arcade.moneyEarned = money
        return money - arcade.moneySpent
    
    def spawnNextWave():
        # force update wave definitions
        arcade.waves = arcadeWaveDefs
        
        arcade.currentWave += 1
        store.arcadeWave = arcade.currentWave
        print("Trying wave " + str(arcade.currentWave))
        if arcade.currentWave >= len(arcade.waves):
            BM.you_win()
        else:
            #BM.battle_bg = "Background/space{!s}.jpg".format(renpy.random.randint(1,9))
            arcade.newWaveThisTurn = True
            musicChanged = False
            arcade.turnsSinceLastWave = 0
            wave = arcade.waves[arcade.currentWave]
            for shipEntry in wave["ships"]:
                posX = randint(shipEntry[1], shipEntry[3])
                posY = randint(shipEntry[2], shipEntry[4])
                create_ship(shipEntry[0], (posX, posY))
            if 'playerMusic' in wave:
                store.PlayerTurnMusic = wave["playerMusic"]
                musicChanged = True
            if 'enemyMusic' in wave:
                store.EnemyTurnMusic = wave["enemyMusic"]
            store.arcadeWaveName = wave["name"]
            if arcade.currentWave == len(arcade.waves) - 1:
                BM.win_when_alone = True
            
            if musicChanged:
                renpy.music.play(store.PlayerTurnMusic)
            renpy.sound.play("sound/beep1.ogg")
            BM.draggable = False
            narrator("Wave " + str(arcade.currentWave + 1) + ": " + store.arcadeWaveName)
            BM.draggable = True
    
    def arcadeStorePurchase(item):
        print("Arcade purchase: " + item.name +", " + item.action[0])
        if item.cost > getArcadeMoneyEarned():
            show_message("Not enough money")
            return
        act = item.action
        if act[0] == "buyUnit":
            print("Trying to make " + act[1]+ " at " + str(store.sunrider.location[0]) + ", " + str(store.sunrider.location[1]))
            ship = create_ship(getattr(store, act[1])(), store.sunrider.location)
            if ship.selection_voice is not None:
                if not type(ship.selection_voice) is list:
                    renpy.music.play(ship.selection_voice,channel = ship.voice_channel)
                else:
                    random_voice = renpy.random.choice(ship.selection_voice)
                    renpy.music.play('sound/Voice/{}'.format(random_voice),channel = ship.voice_channel)
            arcade.spawnedAllyShips.append(ship)
        
        elif act[0] == "buyRepairDrone":
            if store.sunrider.repair_drones >= 8:
                show_message("Already have maximum number of repair drones!")
                return
            store.sunrider.repair_drones += 1
        elif act[0] == "buyTorpedo":
            print(str(store.sunrider.max_rockets) + ", " + str(store.sunrider.max_rockets))
            if store.sunrider.rockets >= store.sunrider.max_rockets:
                show_message("Already have maximum number of torpedoes!")
                return
            store.sunrider.rockets += 1
        elif act[0] == "enableAwakening":       # TODO: safety for if you already have Awaken?
            blackjack.register_weapon(AwakenAsaga())
            if not type(blackjack.buffed_voice) is list:
                renpy.music.play(blackjack.buffed_voice,channel = blackjack.voice_channel)
            else:
                random_voice = renpy.random.choice(blackjack.buffed_voice)
                renpy.music.play('sound/Voice/{}'.format(random_voice),channel = blackjack.voice_channel)
            
        else:   # do nothing
            return
        if item.limit > 0:
            item.limit -= 1
            if (item.limit <= 0):        # TODO: find a way to allow this while also enabling new store items in existing savegame
                arcade.storeItems.remove(item)
                
        arcade.moneySpent += item.cost
        #ui.interact()
        update_stats()
            

label arcade_process_wave:
    if arcade is None:
        $ loadArcadeManager()
    
    if arcade.currentTurn == BM.turn_count:
        return
    
    python:
        arcade.currentTurn = BM.turn_count
        arcade.turnsSinceLastWave += 1
        print("Wave processing for turn " + str(BM.turn_count))
        arcade.newWaveThisTurn = False
        if len(enemy_ships) == 0:
            spawnNextWave()
        elif arcade.currentWave < len(arcade.waves) - 1:
            if arcade.turnsSinceLastWave > arcade.waves[arcade.currentWave+1]["maxDelay"]:     # check maxDelay of the next wave (how long it's willing to wait for us to clear the current one)
                print("Turns since last wave: " + str(arcade.turnsSinceLastWave))
                print("Max delay for wave {0}: {1}".format(arcade.currentWave, arcade.waves[arcade.currentWave]["maxDelay"]))
                spawnNextWave()
    
    return

screen arcade_store_bar:
    if not arcade.showingStore and not BM.missile_moving and not BM.moving and BM.phase == "Player" and sunrider.location != None:
        fixed:
            xpos 540
            imagebutton:
                xpos 0
                ypos 0
                idle 'mods/arcade/Battle UI/arcadestorebar.png'
                hover hoverglow('mods/arcade/Battle UI/arcadestorebar.png')
                action [SetField(arcade,'showingStore',True),Show('arcade_store')]
            text '{!s}'.format(getArcadeMoneyEarned()):
                xanchor 1.0
                xpos 165
                ypos 10
                size 30
                color 'fff'
                outlines [(1,'000',0,0)]

screen arcade_store:
    zorder 1
    modal True
    
    key "mousedown_3" action [Hide('arcade_store'),SetField(arcade,'showingStore',False)]

    fixed:
        xpos 540
        frame:
            background 'mods/arcade/Battle UI/arcadestorebar_window.png'
            at move_down(-590,0)
            vbox:
                spacing 12
                for item in arcade.storeItems:
                    button:
                        xpos 20
                        idle_background 'Battle UI/commandbar_button.png'
                        hover_background hoverglow('Battle UI/commandbar_button.png')
                        action [Function(arcadeStorePurchase, item),Hide('arcade_store'),SetField(arcade,'showingStore',False)]

                        has hbox

                        text item.name.upper():
                            ypos 5
                            min_width 300
                            size 22
                            outlines [(1,'222',0,0)]

                        text str(item.cost):
                            ypos 5
                            xpos 50
                            min_width 50
                            text_align 1.0
    #                       first_indent 150
                            size 18
                            outlines [(1,'222',0,0)]

                        hbox:
                            if BM.show_tooltips == True:
                                frame:
                                    background Solid((0,0,0,200))
                                    xpos 150
                                    ycenter 20

                                    text str(item.tooltip):
                                        xpos 0
                                        ypos 0
                                        size 18
                                        font "Fonts/SourceCodePro-Regular.ttf"
                                        outlines [(1,'000',0,0)]

        imagebutton:
                at move_down(0,590)
                idle 'mods/arcade/Battle UI/arcadestorebar.png'
                hover hoverglow('mods/arcade/Battle UI/arcadestorebar.png')
                action [Hide('arcade_store'),SetField(arcade,'showingStore',False)]
        text '{!s}'.format(getArcadeMoneyEarned()):
            xanchor 1.0
            xpos 165
            ypos 10
            at move_down(10,600,165)
            size 30
            color 'fff'
            outlines [(1,'000',0,0)]