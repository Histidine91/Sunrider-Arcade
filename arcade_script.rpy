label arcade_from_main_menu:
    #stop music fadeout 1.5
    call initialize
    
    hide history
    scene bg black
    show screen quick_menu
    with dissolve
    
    jump arcade_intro

label arcade_intro:
    call arcade_inits from _call_arcade_inits

    # hide screen ship_map
    # show screen battle_screen
    # show screen player_unit_pool_collapsed
    # show screen enemy_unit_pool_collapsed
    
    # call mission_arcade from _call_mission_arcade

    #python:
    #    BM.phase = 'Player'
    #    BM.mission = 'skirmishbattle'
    #    update_stats()
    
    play music "Music/Destinys_Path.ogg"
    show screen leftbuttons
    
    scene bg bridge
        
    $ dshow("ava handonhip neutral neutral neutral")
    with dissolve
    
    ava "We're arriving at the field of battle shortly."
    ava "This will not be an easy challenge. We should upgrade our ryders while we can."
    kay "Alright."
    ava "Do you want an explanation of the rules?"
    
    $ choice1_text = "Yes, please."
    $ choice1_jump = "arcade_tutorial"
    
    $ choice2_text = "I'm good, thanks."
    $ choice2_jump = "arcade_skiptutorial"

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
    play sound "sound/warning.ogg"
    $ dshow('ava handonhip shout neutral angry')
    ava "We're here. Prepare for action."
    kay "All hands, battle stations!"
    
    hide screen leftbuttons
    show screen arcade_store_bar
    
    python:
        BM.mission = 'arcade'   # required to call the correct labels
        BM.battle_bg = "Background/space{!s}.jpg".format(renpy.random.randint(1,9))
        loadArcadeManager()
        
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []
        clean_grid()
        
        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370
        
        store.zoomlevel = 0.65
        BM.phase = 'formation'
        BM.selected = None #if something is selected it won't get shown in the player pool.
        battlemode()
        
        for ship in player_ships:
            ship.location = None
        
        store.PlayerTurnMusic = "mods/arcade/music/Titan.ogg"
        store.EnemyTurnMusic = "mods/arcade/music/Intruders.ogg"
        
        BM.win_when_alone = False
        
        arcade.currentWave = -1
        arcade.turnsSinceLastWave = 0
        arcade.newWaveThisTurn = False
        
    call battle_start

label missionarcade:
    
    call arcade_process_wave

    $BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump missionarcade #loop back
    else:
        pass #continue down
    
label after_arcade:
    # restore after done
    show screen leftbuttons
    hide screen arcade_store_bar

    python:
        #BM.cmd = store.tempcmd
        #BM.money = store.tempmoney
        # store.sunrider.rockets = store.temprockets
        # store.sunrider.repair_drones = store.temprepair_drones
        #if 'original_sunrider' in globals():
        #    player_ships = player_ships_original
        #    sunrider = original_sunrider
        BM.mission = None
        #BM.ships = []
        #for pship in player_ships:
        #    BM.ships.append(pship)
        
        #if not hasattr(arcade,"spawnedAllyShips"):
        #    arcade.spawnedAllyShips = []
        #for ship in arcade.spawnedAllyShips:
        #    BM.ships.remove(ship)
        #    player_ships.remove(ship)
        
    
    hide screen battle_screen
    hide screen commands
    
    $ VNmode()   
    $ end_arcade_score = BM.intel
    
    show screen leftbuttons
    
    hide ava
    scene bg bridge with dissolve
    $dshow("ava handonhair smirk neutral neutral")

    ava "Well done, captain. I wasn't sure we could pull it off."
    kay "Eh, it wasn't too bad. The Lord Gorchnik could have done it in half the time."
    
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
    
    $ renpy.full_restart()
    #jump dispatch