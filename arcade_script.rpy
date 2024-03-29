label arcade_from_main_menu:
    $ arcadefrommenu = True
    call initialize
    python:
        arcadeStoreItems = [CeraGunboatArcadeStore(), UnionFrigateArcadeStore(), UnionBattleshipArcadeStore(), 
                AllianceCruiserArcadeStore(), AllianceBattleshipArcadeStore(), PactEliteArcadeStore(), 
                RyuvianFalconArcadeStore(),FreighterArcadeStore(),RepairDroneArcadeStore(), TorpedoArcadeStore(), 
                AwakeningArcadeStore(), CommandUpgradeArcadeStore(),avc]##N
    jump arcade_main_start_label

label arcade_from_game:
    $ arcadefrommenu = False
    $ player_ships_waitinglist = []
    python:
        arcadeStoreItems = [CeraGunboatArcadeStore(), UnionFrigateArcadeStore(), UnionBattleshipArcadeStore(), 
                AllianceCruiserArcadeStore(), AllianceBattleshipArcadeStore(), PactEliteArcadeStore(), 
                RyuvianFalconArcadeStore(),FreighterArcadeStore(),RepairDroneArcadeStore(), TorpedoArcadeStore(), 
                CommandUpgradeArcadeStore(),enarcade]##N

    jump arcade_main_start_label

label arcade_main_start_label:
    hide history
    scene bg black
    show screen quick_menu
    with dissolve
    
    jump arcade_intro

label arcade_intro:
    call arcade_inits from _call_arcade_inits
    stop music fadeout 1.0
    hide screen ship_map
    # show screen battle_screen
    # show screen player_unit_pool_collapsed
    # show screen enemy_unit_pool_collapsed
    
    # call mission_arcade from _call_mission_arcade

    #python:
    #    BM.phase = 'Player'
    #    BM.mission = 'skirmishbattle'
    #    update_stats()
    pause 1.0
    play music "Music/Destinys_Path.ogg" fadein 1.5
    show screen leftbuttons
    
    scene bg bridge
        
    $ dshow("ava handonhip neutral neutral neutral")
    with dissolve
    
    ava "We're arriving at the field of battle shortly."
    ava "This will not be an easy challenge. We should upgrade our ryders while we can."
    kay "Alright."
    ava "Do you want an explanation of the rules?"

    $ menu_choices = [
                     ["Yes, please.","arcade_tutorial"], 
                     ["I'm good, thanks.","arcade_skiptutorial"], 
                     ]

    
    #$ choice1_text = "Yes, please."
    #$ choice1_jump = "arcade_tutorial"
    
    #$ choice2_text = "I'm good, thanks."
    #$ choice2_jump = "arcade_skiptutorial" ##N

    show screen decision
    pause
    
label arcade_tutorial:
    #$ dshow('ava armscrossed neutral neutral angry')
    #with dissolve
    
    ava "We will have to fight off multiple waves of enemies."
    ava "A new wave will appear the turn after we clean out the preceding one."
    ava "However, if we take too long, the next wave will spawn anyway and dogpile us. Don't let this happen."
    ava "Each enemy ship has a slightly randomized spawn location, so we cannot predict exactly where they'll appear."
    ava "Killing enemies will also earn us money to buy mercenary ships with. These will spawn as close to the Sunrider as they can, and are instantly ready for action."
    ava "The game is won when the final boss is killed."
    ava "Got all that?"
    kay "Yeah, thanks."
    
    jump arcade_intro2
    
label arcade_skiptutorial:
    ava "Very well."
    jump arcade_intro2
    
label arcade_intro2:
    $ renpy.free_memory() 
    play sound "sound/warning.ogg"
    $ dshow('ava handonhip shout neutral angry')
    ava "We're here. Prepare for action."
    kay "All hands, battle stations!"
    
    hide screen leftbuttons
    show screen arcade_store_bar
    $ store.tempmoney = BM.money
    $ store.tempcmd = BM.cmd
    $ store.tempintel = BM.intel
    $ avc.cost = 3000
    if not arcadefrommenu:
        $ avc.cost = 999999
    if not arcadefrommenu:
        $ BM.money = 0
        $ BM.cmd = 0
        $ BM.intel = 0    
    python:
        BM.mission = 'arcade'   # required to call the correct labels
        BM.battle_bg = "Background/space{!s}.jpg".format(renpy.random.randint(1,9))
        loadArcadeManager()
        
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []
        clean_grid()
        arcade.has_won = False
        arcade.early_leave = False
        player_ships_waitinglist = []
        
        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370
        
        store.zoomlevel = 0.65

        BM.phase = 'formation'
        BM.selected = None #if something is selected it won't get shown in the player pool.
        battlemode()
        
        for ship in player_ships:
            ship.location = None
        i = 0
        while i < 1:
            for ship in player_ships:
                if ship.mercenary == True:
                    player_ships.remove(ship)
                    BM.ships.remove(ship)
                    player_ships_waitinglist.append(ship)
                    i += 1    
            if i == 0:
                i = 1
            for ship in player_ships:
                if ship.mercenary == True:
                    i = 0
   

        store.PlayerTurnMusic = "Mod/arcade/music/Titan.ogg"
        store.EnemyTurnMusic = "Mod/arcade/music/Intruders.ogg"
        
        BM.win_when_alone = False
        
        arcade.currentWave = -1
        arcade.turnsSinceLastWave = 0
        arcade.newWaveThisTurn = False
        
    jump battle_start

label missionarcade:
    
    call arcade_process_wave
    
    if arcadeStoreItems[-1].name == "R&D":
        $ arcadeStoreItems[-1].cost = int(1000*1.5**(int(arcade.currentWave)))

    if arcade.has_won != True:
        $BM.battle()  #continue the battle
    
    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump missionarcade #loop back
    else:
        jump after_arcade
    
label after_arcade:
    # restore after done
    #show screen leftbuttons
    hide screen arcade_store_bar
    hide screen arcade_store
    $SetField(arcade,'showingStore',False)

    python:
        end_arcade_score = BM.intel + store.intelspent
        BM.cmd = store.tempcmd
        BM.money = store.tempmoney
        BM.intel = store.tempintel
        store.intelspent = 0
        store.intelN = 0
        store.arcadeRDcost = 3000
        if not arcadefrommenu:
            store.arcadeRDcost = 999999
            store.sunrider.rockets = store.temprockets
            store.paladin.rockets = store.temprocketspaladin
            store.sunrider.repair_drones = store.temprepair_drones 

        #if 'original_sunrider' in globals():
        #    player_ships = player_ships_original
        #    sunrider = original_sunrider
        BM.mission = None
        BM.ships = []
        for pship in player_ships:
            BM.ships.append(pship)
        
        if not hasattr(arcade,"spawnedAllyShips"):
            arcade.spawnedAllyShips = []
        for ship in arcade.spawnedAllyShips:
            BM.ships.remove(ship)
            player_ships.remove(ship)
    python:
        i = 0
        while i < 1:
            for ship in player_ships_waitinglist:
                if ship.mercenary == True:
                    player_ships_waitinglist.remove(ship)
                    BM.ships.append(ship)
                    player_ships.append(ship)
                    i += 1    

            for ship in player_ships_waitinglist:
                if ship.mercenary == True:
                    i = 0
            if len(player_ships_waitinglist) == 0:
                i += 1
    
    hide screen battle_screen
    hide screen commands
    
    $ VNmode()   

    
    #show screen leftbuttons
    
    hide ava
    scene bg bridge with dissolve

    if arcade.early_leave == False:
        $dshow("ava handonhair smirk neutral neutral")
        with dissolve
        ava "Well done, captain. I wasn't sure we could pull it off."
        kay "Eh, it wasn't too bad. The Lord Gorchnik could have done it in half the time."
    else:
        $ dshow("ava handonhip neutral neutral neutral")
        with dissolve
        ava "Alright, let's try again later."
        
    python:
        if persistent.arcade_high_score is None:
            persistent.arcade_high_score = 0
        difficulty_mod = BM.lowest_difficulty + 1
        if (BM.lowest_difficulty == 5):
            difficulty_mod = BM.lowest_difficulty + 3       # compensate for space whale tax
        score = end_arcade_score * (difficulty_mod)/(BM.turn_count + 5)
    
    "Score: {b}[score]{/b}\n(ending intel * (difficulty mod) / (turns taken + 5))"
    
    python:
        if score > persistent.arcade_high_score:
            previousScore = persistent.arcade_high_score
            narrator("Wow! A new high score!!\n(previous: " + str(previousScore) + ")")
            persistent.arcade_high_score = score
    
    kay "Well, we're done here. Retrieve our ryders and prepare to warp out."
    
    scene black with dissolvemedium
    
    "Until next time..."
    python:
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

    if arcadefrommenu:
        $ renpy.full_restart()
    else:
        play music "Mod/arcade/music/Colors_Of_An_Orchestra.ogg"
        jump dispatch