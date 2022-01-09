init 5 python: # needs to be lower than 6 to ensure Tweakpack's custom_fire settings gets the weapon defs here
    global BM
    if not hasattr(store,'intelN'):
        store.intelN = 0
    if not hasattr(store,'intelspent'):
        store.intelspent = 0
    if not hasattr(store,'arcadeRDcost'):
        store.arcadeRDcost = 2000

    #talk_buttons.append(["MainMissionCompleted() > 14",'avajagY','captainsloft','arcade_from_game'])

    arcadeWaveDefs = [
            {
                'name' : 'Back to Basics',  #1
                'maxDelay' : 0,
                'ships' : {
                        ("PactCruiser", 12, 7, 13, 8),      #ship, x1, y1, x2, y2
                        ("PactCruiser", 12, 10, 13, 11),
                        ("MissileFrigate", 14, 6, 15, 8),
                        ("MissileFrigate", 14, 10, 15, 12),
                        ("PactMook", 10, 5, 11, 7),
                        ("PactMook", 10, 6, 11, 8),
                        ("PactMook", 10, 9, 11, 11),
                        ("PactMook", 10, 10, 11, 12),
                        ("PactBomber", 10, 4, 11, 6),
                        ("PactBomber", 10, 11, 11, 13),
                }
            },
            {
                'name' : 'Task Force Red',  #2
                'maxDelay' : 2,
                'ships' : {
                        ("PactBattleship", 12, 5, 13, 7),
                        ("PactBattleship", 12, 11, 13, 13),
                        ("PactCruiser", 14, 6, 15, 8),
                        ("PactCruiser", 14, 10, 15, 12),
                        ("PactFastCruiser", 10, 5, 11, 7),
                        ("PactFastCruiser", 10, 11, 11, 13),
                        ("MissileFrigate", 11, 3, 12, 5),
                        ("MissileFrigate", 11, 12, 12, 14),
                        ("MissileFrigate", 11, 4, 12, 6),
                        ("MissileFrigate", 11, 11, 12, 13),
                }
            },
            {
                'name' : 'RRRRRRR!',        #3
                'playerMusic' : 'Music/Danger.ogg',
                'enemyMusic' : 'Music/VolatileReaction.ogg',
                'maxDelay' : 2,
                'ships' : {
                        ("PirateDestroyer", 12, 5, 13, 7),
                        ("PirateDestroyer", 12, 11, 13, 13),
                        ("PirateDestroyer", 12, 6, 13, 8),
                        ("PirateDestroyer", 12, 12, 13, 14),
                        ("PirateIronhog", 14, 4, 15, 6),
                        ("PirateIronhog", 14, 13, 15, 15),
                        ("PirateGrunt", 10, 5, 11, 7),
                        ("PirateGrunt", 10, 6, 11, 8),
                        ("PirateGrunt", 10, 9, 11, 11),
                        ("PirateGrunt", 10, 10, 11, 12),
                        ("PirateBomber", 10, 4, 11, 6),
                        ("PirateBomber", 10, 11, 11, 13),
                }
            },
            {
                'name' : 'Carrier Has Arrived',  #4
                'maxDelay' : 3,
                'ships' : {
                        ("PactCarrier", 14, 6, 15, 7),
                        ("PactCarrier", 14, 9, 15, 9),
                        ("PactCarrier", 14, 12, 15, 13),
                        ("PactBattleship", 14, 6, 15, 8),
                        ("PactBattleship", 14, 10, 15, 12),
                        ("PactDestroyer", 12, 4, 13, 6),
                        ("PactDestroyer", 12, 13, 13, 15),
                        ("PactMook", 11, 4, 12, 6),
                        ("PactMook", 11, 11, 12, 13),
                        ("PactMook", 11, 5, 12, 7),
                        ("PactMook", 11, 10, 12, 12),
                        ("PactBomber", 12, 4, 13, 5),
                        ("PactBomber", 12, 11, 13, 12),
                }
            },
            {
                'name' : 'Rise of Ryuvia',  #5
                'maxDelay' : 3,
                'playerMusic' : 'Music/Epic_Action_Hero.ogg',
                'enemyMusic' : 'Music/MarduksWrath.ogg',
                'ships' : {
                        ("SeraphimEnemy", 14, 6, 15, 7),
                        ("SeraphimEnemy", 14, 9, 15, 9),
                        ("SeraphimEnemy", 14, 12, 15, 13),
                        ("Nightmare", 13, 5, 14, 7),
                        ("Nightmare", 13, 11, 14, 13),
                        ("RyuvianCruiser", 11, 3, 12, 5),
                        ("RyuvianCruiser", 11, 12, 12, 14),
                        ("RyuvianCruiser", 12, 5, 13, 6),
                        ("RyuvianCruiser", 12, 10, 13, 11),
                }
            },
            {
                'name' : 'L337 Krew',  #6
                'maxDelay' : 4,
                'ships' : {
                        ("PactAssaultCarrier", 14, 7, 15, 9),
                        ("PactAssaultCarrier", 14, 10, 15, 12),
                        ("PactSupport", 14, 6, 15, 8),
                        ("PactSupport", 14, 11, 15, 13),
                        ("PactDestroyer", 12, 4, 13, 6),
                        ("PactDestroyer", 12, 13, 13, 15),
                        ("PactBomber", 11, 3, 12, 5),
                        ("PactBomber", 11, 12, 12, 14),
                        ("PactElite", 10, 4, 11, 6),
                        ("PactElite", 10, 11, 11, 13),
                        ("PactElite", 11, 6, 13, 8),
                        ("PactElite", 11, 9, 13, 11),
                        ("PactFastCruiser", 11, 5, 12, 7),
                        ("PactFastCruiser", 11, 11, 12, 13),
                        ("PactFastCruiser", 12, 6, 13, 7),
                        ("PactFastCruiser", 12, 11, 13, 12),
                }
            },
            {
                'name' : 'Cry Havoc',  #7
                'maxDelay' : 5,
                'playerMusic' : 'Mod/arcade/music/Powerful.ogg',
                'enemyMusic' : 'Mod/arcade/music/Sui_Generis.ogg',
                'ships' : {
                        ("PirateIronhog", 14, 6, 15, 7),
                        ("Havoc", 14, 9, 15, 9),
                        ("PirateIronhog", 14, 12, 15, 13),
                        ("PactSupport", 14, 6, 15, 8),
                        ("PactSupport", 14, 11, 15, 13),
                        ("PactCarrier", 13, 4, 14, 6),
                        ("PactCarrier", 13, 13, 14, 15),
                        ("PirateGrunt", 11, 3, 12, 5),
                        ("PirateGrunt", 11, 12, 12, 14),
                        ("PirateGrunt", 11, 4, 12, 6),
                        ("PirateGrunt", 11, 11, 12, 13),
                        ("PirateBomber", 10, 4, 11, 6),
                        ("PirateBomber", 10, 11, 11, 13),
                        ("PactFastCruiser", 12, 7, 13, 8),
                        ("PactFastCruiser", 12, 10, 13, 11),
                }
            },
            {
                'name' : 'Fighting Falcon',  #8
                'maxDelay' : 5,
                'ships' : {
                        ("RyuvianFalconEnemy", 14, 9, 15, 9),
                        ("SeraphimEnemy", 14, 6, 15, 7),
                        ("SeraphimEnemy", 14, 12, 15, 13),
                        ("Nightmare", 13, 6, 14, 8),
                        ("Nightmare", 13, 11, 14, 13),
                        ("Nightmare", 12, 5, 13, 7),
                        ("Nightmare", 12, 12, 13, 14),
                        ("RyuvianCruiser", 10, 4, 11, 6),
                        ("RyuvianCruiser", 10, 11, 11, 13),
                        ("RyuvianCruiser", 11, 4, 13, 5),
                        ("RyuvianCruiser", 11, 11, 13, 12),
                        ("RyuvianCruiser", 11, 6, 12, 8),
                        ("RyuvianCruiser", 11, 9, 12, 11),
                }
            },
            {
                'name' : 'Consolidation',  #9
                'maxDelay' : 6,
                'playerMusic' : 'Mod/arcade/music/Overpowered.ogg',
                'enemyMusic' : 'Mod/arcade/music/Gore_and_Sand.ogg',
                'ships' : {
                        ("PactDestroyer", 14, 6, 15, 7),
                        ("PactAssaultCarrier", 14, 9, 15, 9),
                        ("PactDestroyer", 14, 12, 15, 13),
                        ("PactSupport", 14, 6, 15, 8),
                        ("PactSupport", 14, 11, 15, 13),
                        ("PactBattleship", 13, 6, 14, 8),
                        ("PactBattleship", 13, 10, 14, 12),
                        ("Nightmare", 15, 5, 16, 7),
                        ("Nightmare", 15, 12, 16, 14),
                        ("PactElite", 11, 3, 12, 5),
                        ("PactElite", 11, 12, 12, 14),
                        ("PirateDestroyer", 11, 4, 12, 6),
                        ("PirateDestroyer", 11, 11, 12, 13),
                        ("Arcadius", 10, 4, 11, 6),
                        ("Arcadius", 10, 11, 11, 13),
                        ("RyuvianCruiser", 12, 4, 13, 5),
                        ("RyuvianCruiser", 12, 11, 13, 12),
                }
            },
            {
                'name' : 'For We Are Many',  #10
                'maxDelay' : 7,
                'playerMusic' : 'Music/The_Bladed_Druid.ogg',
                'enemyMusic' : 'Mod/arcade/music/Posthumus_Regium.ogg',
                'ships' : {
                        ("PactCarrier", 16, 7, 17, 7),
                        ("LegionArcade", 16, 9, 16, 9),
                        ("PactCarrier", 16, 12, 17, 12),
                        ("PirateIronhog", 14, 5, 15, 7),
                        ("PirateIronhog", 14, 12, 15, 14),
                        ("PactAssaultCarrier", 15, 6, 16, 8),
                        ("PactAssaultCarrier", 15, 11, 16, 13),
                        ("PirateBase", 14, 7, 14, 7),
                        ("PirateBase", 14, 12, 14, 12),
                        ("PactCruiser", 12, 6, 13, 8),
                        ("PactCruiser", 12, 7, 13, 9),
                        ("PactCruiser", 12, 9, 13, 11),
                        ("PactCruiser", 12, 10, 13, 12),
                        ("Arcadius", 11, 3, 12, 5),
                        ("Arcadius", 11, 12, 12, 14),
                        #("PactElite", 11, 4, 12, 6),
                        #("PactElite", 11, 11, 12, 13),
                        #("RyuvianCruiser", 10, 4, 11, 6),
                        #("RyuvianCruiser", 10, 11, 11, 13),
                        ("Arcadius", 12, 4, 13, 5),
                        ("Arcadius", 12, 11, 13, 12),
                }
            },
            {
                'name' : 'Destiny Ascension',  #11
                'maxDelay' : 9,
                'playerMusic' : 'Music/The_Bladed_Druid.ogg', ##N 
                'enemyMusic' : 'Music/Posthumus_Regium.ogg', ##N
                'ships' : {
                        ("PactCarrier", 16, 7, 17, 7),
                        ("Nightmare_Ascendant_Arcade", 16, 9, 16, 9),
                        ("PactCarrier", 16, 12, 17, 12),
                        ("Havoc", 13, 5, 14, 7),
                        ("Havoc", 13, 12, 14, 14),
                        ("PactProtoCarrier", 15, 6, 16, 8),
                        ("PactProtoCarrier", 15, 11, 16, 13),
                        ("PactOutpostArcade", 14, 7, 14, 7),
                        ("PactOutpostArcade", 14, 12, 14, 12),
                        ("Nightmare_Flierdrone_Arcade", 12, 7, 12, 7),
                        ("Nightmare_Flierdrone_Arcade", 13, 8, 13, 8),
                        ("Nightmare_Flierdrone_Arcade", 13, 10, 13, 10),
                        ("Nightmare_Flierdrone_Arcade", 12, 11, 12, 11),
                        ("PactSupport", 11, 3, 12, 5),
                        ("PactSupport", 11, 12, 12, 14),
                        ("RyuvianCruiser", 11, 4, 12, 6),
                        ("RyuvianCruiser", 11, 11, 12, 13),
                        ("RyuvianCruiser", 10, 4, 11, 6),
                        ("RyuvianCruiser", 10, 11, 11, 13),
                        ("Nightmare_Flierdrone_Arcade", 12, 5, 13, 5),
                        ("Nightmare_Flierdrone_Arcade", 12, 11, 13, 11),
                }
            },
        ]

    class MunitionsFreighter(Battleship):
        def __init__(self):
            super(MunitionsFreighter, self).__init__()
            self.stype = 'Ship'
            self.name = 'Munitions Freighter'
            self.support = True  #signifies to the AI this unit uses support skills
            self.animation_name = 'mochi'
            self.faction = 'Player'
            self.mercenary = True
            self.max_hp = 1000
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 10
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.move_cost = 40
            self.hate = 50
            self.evasion = 0
            self.default_weapon_list = [FreighterReloadMissile()]
            self.lbl = Image('Battle UI/label_mochi.png')  #this is the battle avatar
            self.portrait = None
            self.flak = 0
            self.flak_range = 0

            self.voice_channel = "othvoice"
            self.selection_voice = ['sound/beep1.ogg']
            self.moveforward_voice = ['sound/beep2.ogg']
            self.movebackward_voice = ['sound/beep2.ogg']
            self.buffed_voice = ['sound/beep2.ogg']
            self.cursed_voice = ['sound/beep2.ogg']
                
    # test
    class LegionArcade(Legion):
        def __init__(self):
            super(LegionArcade, self).__init__()
            self.stype = 'Assault Carrier'
            self.spawns = [
                ( PactElite,20,[ PACTEliteLaser(),PACTEliteMissile(),PACTEliteAssault(),PACTEliteMelee() ] ),
                ( PactSupport,20,[ PactRepair(), DisableLite(), PactRestore(), PactFlakOff(), PactShutOff() ] )
                ]
            self.max_en = 120
            self.en = self.max_en
            self.default_weapon_list = [LegionSuperLaser(),LegionLaser(),LegionKinetic(),LegionMissile()]
                
    class Nightmare_Ascendant_Arcade(Nightmare_Ascendant):
        def __init__(self):
            super(Nightmare_Ascendant_Arcade, self).__init__()
            self.default_weapon_list = [BossRocket(),BossLaser(),BossMelee()]
            self.max_missiles = 2
            self.max_rockets = 2
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.brain = BossAI(self)
            self.name = "Boss"
            self.blbl = im.MatrixColor('Battle UI/label_nightmareascendant.png',im.matrix.hue(265))  #temp image
            self.lbl = self.blbl

    class Nightmare_Flierdrone_Arcade(Nightmare_Flierdrone):
        def __init__(self):
            super(Nightmare_Flierdrone_Arcade, self).__init__()
            self.blbl = im.MatrixColor('Battle UI/label_nightmareflier.png',im.matrix.hue(265))  #this is the battle avatar
            self.lbl = self.blbl
            
            
    class PactOutpostArcade(PactOutpost):
        def __init__(self):
            super(PactOutpostArcade, self).__init__()
            self.stype = 'Station'
            self.name = 'PACT Adv Outpost'
            self.support = True  #signifies to the AI this unit uses support skills
            self.max_hp = 1200
            self.hp = self.max_hp
            self.max_en = 120
            self.en = self.max_en
            self.base_armor = 30
            self.armor = self.base_armor
            self.money_reward = 750
            self.boss = False
            self.default_weapon_list = [PACTCruiserLaser(),PACTCruiserKinetic(),PactRepair(),AccUp()]
    
    # piercing laser like Nightmare Ascendant has
    class LegionSuperLaser(BossLaser):
        #pierces through enemies and ignores 30 points of shielding.
        def __init__(self):
            BossLaser.__init__(self)
            self.name = 'Legion Superlaser'
            self.ignore_shielding = 30 #subtractive
            self.damage = 320
            self.energy_use = 100
            self.shot_count = 1
            self.accuracy = 100
            self.wtype = 'Laser'
        
    class FreighterReloadMissile(Support):
        def __init__(self):
            Support.__init__(self)
            self.energy_use = 60
            self.modifies = 'missiles'
            #self.applied_buff = MissileReloadB
            self.buff_strength = 1
            self.buff_duration = 1
            self.hate_penalty = 80
            self.name = 'Reload'
            self.lbl = Image('Battle UI/button_missile.png')
            self.tooltip = """
            Restocks one unit of missile ammo for the target.
            Has a range of three hexes."""
            
        def fire(self,parent,target,counter = False,hidden=False):
            if self.parent is None: self.parent = parent
            
            if target.max_missiles <= 0:
                show_message("{0} has no missiles!".format(target.name))
                return
            if (target.missiles >= target.max_missiles):
                show_message("{0} already has full magazines!".format(target.name))
                return
            
            #take away energy
            if parent.en < self.energy_cost(parent):  #energy handling
                return 'no energy'
            else:
                parent.en = increment_attribute(parent,'en',-self.energy_cost(parent))
            
            target.missiles += 1
            BM.battle_log_insert(['support', 'debuff'], "{0} reloading missiles for {1}".format(parent.name, target.name))
            target.update_stats()
            
            #animation
            if not hidden:
                target.getting_buff = True
                BM.selectedmode = False
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
                if BM.phase == 'Player':
                    if not target == parent and target.faction == 'Player':
                        if target.pilot is not None: ##N
                            if target != self.parent:
                                target.voice('HitBuff')
                        else:
                            if target.buffed_voice is not None:
                                a = renpy.random.randint(0,len(target.buffed_voice)-1)
                                renpy.music.play('{}'.format(target.buffed_voice[a]),channel = target.voice_channel)
                                del a

                           #if target.buffed_voice is not None:
                           #     renpy.music.play( renpy.random.choice(target.buffed_voice), channel = target.voice_channel )
                message = "{0} reloading missiles for {1}".format(parent.name, target.name) # we can't make this only display when in enemy phase; it hides the buff anim
                show_message(message)
                target.getting_buff = False
                if BM.phase == 'Player':
                    BM.selectedmode = True
                    BM.targetingmode = False
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
            return 0
    
    # Arcade store item definitions
    class ArcadeStoreItem(store.object):
        id = "id"
        name = "Generic Item"
        tooltip = "tooltip"
        cost = 0
        #action = bla
        limit = -1
        
    class CeraGunboatArcadeStore(ArcadeStoreItem):
        id = "ceraGunboat"
        name = "Cera Gunboat"
        tooltip = "Fast light combatant with pew-pew assault guns."
        cost = 1500
        limit = 4
        action = ("buyUnit", "CeraGunboat")
        
    class UnionFrigateArcadeStore(ArcadeStoreItem):
        id = "unionFrigate"
        name = "Union Frigate"
        tooltip = "Light laser platform that can disrupt enemy shields."
        cost = 1500
        limit = 3
        action = ("buyUnit", "UnionFrigate")
                
    class UnionBattleshipArcadeStore(ArcadeStoreItem):
        id = "unionBattleship"
        name = "Union Battleship"
        tooltip = "Big ship with big lasers. Can pull other big ships."
        cost = 7000
        limit = 1
        action = ("buyUnit", "UnionBattleship")
    
    class AllianceCruiserArcadeStore(ArcadeStoreItem):
        id = "allianceCruiser"
        name = "Alliance Cruiser"
        tooltip = "Powerful, versatile medium warship."
        cost = 4000
        limit = 2
        action = ("buyUnit", "AllianceCruiser")
                
    class AllianceBattleshipArcadeStore(ArcadeStoreItem):
        id = "allianceBattleship"
        name = "Alliance Battleship"
        tooltip = "Heavy vessel with a really big cannon."
        cost = 8000
        limit = 1
        action = ("buyUnit", "AllianceBattleship")
                
    class RyuvianFalconArcadeStore(ArcadeStoreItem):
        id = "ryuvianFalcon"
        name = "Ryuvian Falcon"
        tooltip = "Fast, decently protected, and mean as hell."
        cost = 3000
        limit = 2
        action = ("buyUnit", "RyuvianFalcon")
    
    class PactEliteArcadeStore(ArcadeStoreItem):
        id = "PactElite"
        name = "PACT Elite"
        tooltip = "Advanced ryder, lethal in close combat."
        cost = 3000
        limit = 2
        action = ("buyUnit", "FriendlyPactElite")
    
    class FreighterArcadeStore(ArcadeStoreItem):
        id = "freighter"
        name = "Munitions Freighter"
        tooltip = "A freighter that can reload missiles of friendly units."
        cost = 4000
        limit = 2
        action = ("buyUnit", "MunitionsFreighter")
    
    class RepairDroneArcadeStore(ArcadeStoreItem):
        id = "repairdrone"
        name = "Repair Drone"
        tooltip = "Adds 1 repair drone to the Sunrider's stocks."
        cost = 800
        action = ("buyRepairDrone",)
                
    class TorpedoArcadeStore(ArcadeStoreItem):
        id = "torpedo"
        name = "Torpedo"
        tooltip = "Adds 1 torpedo to the Sunrider's stocks."
        cost = 600
        action = ("buyTorpedo",)
    
    class AwakeningArcadeStore(ArcadeStoreItem):
        id = "awakening"
        name = "Awakening"
        tooltip = "Enables Asaga's Awakening ability."
        cost = 3000
        limit = 1
        action = ("enableAwakening",)
                
    class CommandUpgradeArcadeStore(ArcadeStoreItem):
        id = "cmdUpgrade"
        name = "Command Boost"
        tooltip = "Increases max Command Points by 1000."
        cost = 6000
        limit = 1
        action = ("addCMDPoints", 1000)

    class visitResearch(ArcadeStoreItem): ##N
        id = "vResearch" ##N
        name = "R&D" ##N
        tooltip = "Let's you visit R&D for upgrading your units" ##N
        cost = store.arcadeRDcost ##N
        action = ("visitResearch",) ##N
    avc = visitResearch()
    class endarcade(ArcadeStoreItem): ##N
        id = "endearcade" ##N
        name = "Quit" ##N
        tooltip = "Quit the during arcade." ##N
        cost = 0 ##N
        action = ("endarcade",) ##N
    enarcade = endarcade()
    class Researchvisit(ArcadeStoreItem): ##N
        id = "viResearch" ##N
        name = "R&D" ##N
        tooltip = "Let's you visit R&D for upgrading your units" ##N
        cost = store.arcadeRDcost ##N
        action = ("visitResearch") ##N
                
        if not hasattr(store,'arcadeStoreItems'): arcadeStoreItems = []##N
                
label arcade_inits:
    python:
        
        store.tempmoney = BM.money
        store.tempcmd = BM.cmd
        store.tempintel = BM.intel
        if not hasattr(store,'arcadefrommenu'):
            arcadefrommenu = False     
        # TODO make it not crash
        if not arcadefrommenu:
        #    player_ships_original = player_ships
        #    original_sunrider = sunrider
            store.temprockets = store.sunrider.rockets
            store.temprepair_drones = store.sunrider.repair_drones
            store.temprocketspaladin = store.paladin.rockets
        if arcadefrommenu:
            arcadefrommenu = True
            BM.money = 0
            BM.cmd = 0
            BM.intel = 30000
            BM.orders['SHORT RANGE WARP'] = [750,'short_range_warp']
            BM.orders["RESURRECTION"] = [2500,'resurrection']

            sunrider_weapons = [SunriderLaser(),SunriderKinetic(),SunriderMissile(),SunriderRocket(),SunriderAssault(),SunriderPulse()]
            sunrider = create_ship(Sunrider(),(1,1),sunrider_weapons)
            sunrider.repair_drones = 1

            blackjack_weapons = [BlackjackMelee(),BlackjackLaser(),BlackjackAssault(),BlackjackMissile(),BlackjackPulse()]
            blackjack = create_ship(BlackJack(),(1,2),blackjack_weapons)

            liberty_weapons = [LibertyLaser(),Repair(),AccUp(),Disable(),FlakOff(),ShutOff()]
            liberty = create_ship(Liberty(),(5,7),liberty_weapons)

            phoenix_weapons = [PhoenixAssault(),PhoenixMelee(),Stealth()]
            phoenix = create_ship(Phoenix(),(9,5),phoenix_weapons)

            bianca_weapons = [BiancaAssault(),GravityGun(),AccDown(),DamageUp(),Restore()]
            bianca = create_ship(Bianca(),(14,7),bianca_weapons)

            seraphim_weapons = [SeraphimKinetic(),Awaken()]
            seraphim = create_ship(Seraphim(),(6,8),seraphim_weapons)

            paladin_weapons = [PaladinMissile(),PaladinAssault(),PaladinKinetic(), Taunt()]
            paladin = create_ship(Paladin(),(9,8),paladin_weapons)
        
        #store.sunrider = sunrider
        #store.blackjack = blackjack
        #store.liberty = liberty
        #store.phoenix = phoenix
        #store.bianca = bianca
        #store.seraphim = seraphim
        #store.paladin = paladin
        
            process_upgrade(sunrider,"max_hp",10)
            process_upgrade(sunrider,"max_en",7)
            process_upgrade(sunrider,"evasion",1)
            process_upgrade(sunrider,"kinetic_dmg",6)
            process_upgrade(sunrider,"kinetic_acc",3)
            process_upgrade(sunrider,"kinetic_cost",4)
            process_upgrade(sunrider,"energy_dmg",6)
            process_upgrade(sunrider,"energy_acc",3)
            process_upgrade(sunrider,"energy_cost",4)
            process_upgrade(sunrider,"missile_dmg",6)
            process_upgrade(sunrider,"missile_eccm",2)
            process_upgrade(sunrider,"missile_cost",2)
            process_upgrade(sunrider,"max_missiles",3)
            process_upgrade(sunrider,"flak",3)
            process_upgrade(sunrider,"base_armor",2)

            process_upgrade(blackjack,"max_hp",3)
            process_upgrade(blackjack,"max_en",3)
            process_upgrade(blackjack,"evasion",1)
            process_upgrade(blackjack,"kinetic_dmg",3)
            process_upgrade(blackjack,"kinetic_acc",3)
            process_upgrade(blackjack,"kinetic_cost",2)
            process_upgrade(blackjack,"energy_dmg",3)
            process_upgrade(blackjack,"energy_acc",3)
            process_upgrade(blackjack,"energy_cost",2)
            process_upgrade(blackjack,"missile_dmg",3)
            process_upgrade(blackjack,"missile_eccm",1)
            process_upgrade(blackjack,"missile_cost",1)
            process_upgrade(blackjack,"max_missiles",2)
            process_upgrade(blackjack,"melee_dmg",3)
            process_upgrade(blackjack,"melee_acc",1)
            process_upgrade(blackjack,"melee_cost",1)
            process_upgrade(blackjack,"flak",2)
            process_upgrade(blackjack,"base_armor",2)

            process_upgrade(liberty,"max_hp",3)
            process_upgrade(liberty,"max_en",6)
            process_upgrade(liberty,"evasion",2)
            process_upgrade(liberty,"energy_dmg",1)
            process_upgrade(liberty,"energy_acc",1)
            process_upgrade(liberty,"energy_cost",1)
            process_upgrade(liberty,"shield_generation",2)
            process_upgrade(liberty,"shield_range",2)
            process_upgrade(liberty,"base_armor",1)

            process_upgrade(phoenix,"max_hp",3)
            process_upgrade(phoenix,"max_en",3)
            process_upgrade(phoenix,"evasion",3)
            process_upgrade(phoenix,"kinetic_dmg",3)
            process_upgrade(phoenix,"kinetic_acc",3)
            process_upgrade(phoenix,"kinetic_cost",2)
            process_upgrade(phoenix,"melee_dmg",3)
            process_upgrade(phoenix,"melee_acc",2)
            process_upgrade(phoenix,"melee_cost",2)
            process_upgrade(phoenix,"flak",2)
            process_upgrade(phoenix,"base_armor",1)

            process_upgrade(bianca,"max_hp",3)
            process_upgrade(bianca,"max_en",5)
            process_upgrade(bianca,"evasion",1)
            process_upgrade(bianca,"kinetic_dmg",2)
            process_upgrade(bianca,"kinetic_acc",2)
            process_upgrade(bianca,"kinetic_cost",1)
            process_upgrade(bianca,"shield_generation",2)
            process_upgrade(bianca,"shield_range",1)
            process_upgrade(bianca,"base_armor",1)

            process_upgrade(seraphim,"max_hp",3)
            process_upgrade(seraphim,"max_en",3)
            process_upgrade(seraphim,"evasion",1)
            process_upgrade(seraphim,"kinetic_dmg",7)
            process_upgrade(seraphim,"kinetic_acc",2)
            process_upgrade(seraphim,"kinetic_cost",3)
            process_upgrade(seraphim,"base_armor",1)
        
            process_upgrade(paladin,"max_hp",3)
            process_upgrade(paladin,"max_en",3)
            process_upgrade(paladin,"evasion",1)
            process_upgrade(paladin,"kinetic_dmg",4)
            process_upgrade(paladin,"kinetic_acc",2)
            process_upgrade(paladin,"kinetic_cost",3)
            process_upgrade(paladin,"missile_dmg",2)
            process_upgrade(paladin,"missile_eccm",2)
            process_upgrade(paladin,"missile_cost",2)
            process_upgrade(paladin,"max_missiles",1)
            process_upgrade(paladin,"flak",1)
            process_upgrade(paladin,"base_armor",2)
        
        # grav gun booster
            store.bianca.weapons[1].energy_use = 40
            store.bianca.weapons[1].keep_after_reset['energy_use'] = 40
        
        # Sunrider shield
            store.sunrider.shield_generation = 15
            store.sunrider.shields = store.sunrider.shield_generation
            store.sunrider.shield_range = 0
        
        # repair booster
            if not hasattr(store,'chigara_repair'):store.chigara_repair = liberty.weapons[1]
            store.chigara_repair.damage = 500
            store.chigara_repair.keep_after_reset['damage'] = 500
            store.chigara_repair.energy_use = 70
            store.chigara_repair.keep_after_reset['energy_use'] = 70
            
        # quantum torps
            if not hasattr(store,'sunrider_rocket'):store.sunrider_rocket = sunrider.weapons[3]
            store.sunrider_rocket.damage = 1200
            store.sunrider_rocket.keep_after_reset['damage'] = 1200
        
            store.legion_destroyed = False

    return

init 9 python:
    def start_arcade():
        renpy.hide_screen('main_menu')
        arcadefrommenu = True
        renpy.jump("arcade_from_main_menu")
