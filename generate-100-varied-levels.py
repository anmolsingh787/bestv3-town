import json

# ==============================================================================
# 100 UNIQUE, THEMATIC, HIGHLY ENGAGING LEVELS GENERATOR
# Each level has 5 completely distinct, handcrafted tactical waves!
# ==============================================================================

chapters = [
    ("THE GREEN INVASION", "GREENWOOD", 0xffffff, [
        ("First Light", "GORBAK · SCOUT CHIEFTAIN"),
        ("Outpost Skirmish", "RUST-BLADE SKORR"),
        ("Thorny Path", "THORN-TOOTH BRUTE"),
        ("River Ambush", "RIVER-FANG REAVER"),
        ("Chieftain's Hill", "WAR-BOSS GORBAK")
    ]),
    ("FOREST OF WHISPERS", "WHISPERING WOODS", 0xe6f2d8, [
        ("Silent Pines", "SNARL · WOODS TRACKER"),
        ("Mossy Ruins", "BOMB-TOSS KRAG"),
        ("Shadow Thicket", "ELDER SHADOWFANG"),
        ("Creaking Hollow", "BARK-HIDE TANK"),
        ("Heart of the Forest", "WAR-CHIEF SNARL")
    ]),
    ("ASHEN WASTES", "ASHEN PLAIN", 0xefebe9, [
        ("Cinder Approach", "CINDER-CLAW SCOUT"),
        ("Smoldering Gulch", "MALKOR THE HEX-WEAVER"),
        ("Burnt Ridge", "ASH-GUARD BULWARK"),
        ("Fire-Spitter Trail", "BLAZE-FANG REAVER"),
        ("The Ash Citadel", "WARLORD CINDER-TOOTH")
    ]),
    ("SULPHUR MINES", "SULPHUR MINES", 0xfff9c4, [
        ("Shaft Entrance", "MINER-KING DROK"),
        ("Deep Quarry", "NITRO-RUNNER SKULK"),
        ("Gas Pockets", "BLAST-CHIEF GRIMJAW"),
        ("Boiling Slag", "SULPHUR BRUTE TANK"),
        ("The Mine Core", "WARLORD GRIMJAW")
    ]),
    ("VOLCANIC PEAKS", "MAGMA CRAGS", 0xffccbc, [
        ("Obsidian Slope", "MAGMA-CRUSHER VOLK"),
        ("Lava Bridges", "PYRO-CHIEF KRULL"),
        ("Caldera Edge", "MOLTEN SHIELD-LORD"),
        ("Brimstone Fall", "LAVA-FANG REAVER"),
        ("Volcano Summit", "WARLORD VOLK")
    ]),
    ("DRAGON SPIRES", "WYVERN ROOST", 0xe1f5fe, [
        ("High Perch", "WYVERN-TAMER TORK"),
        ("Sky Gate", "DRAKE-WING SKYLORD"),
        ("Clifftop Nests", "WIND-CLEAVER REAVER"),
        ("Raptor Crag", "SKY-CHIEF KRAKOR"),
        ("The Dragon Throne", "DRAKE-OVERLORD KRAKOR")
    ]),
    ("SHADOW REALM", "SHADOW VALE", 0xede7f6, [
        ("Twilight Border", "NIGHT-STALKER VEIL"),
        ("Gloom Ravine", "SHADOW-HEX SHAMAN"),
        ("Echoing Chasm", "VOID-BLADE ASSASSIN"),
        ("Veil of Sorrows", "DREAD-STALKER REAVER"),
        ("Seat of Night", "SHADOW-LORD VEX")
    ]),
    ("NIGHTFALL MARSHES", "MURKWATER FENS", 0xd7ccc8, [
        ("Bog Approach", "MUD-CRAWLER SCOUT"),
        ("Poison Willow", "VENOM-HEX SHAMAN"),
        ("Quicksand Trap", "SWAMP-KING BOG-GUT"),
        ("Leech Fen", "SLIME-HIDE BRUTE"),
        ("The Witch Tree", "WARLORD BOG-GUT")
    ]),
    ("BLOOD CITADEL", "CRIMSON CITADEL", 0xffcdd2, [
        ("Outer Courtyard", "BLOOD-KNIGHT VARG"),
        ("Iron Portcullis", "SHIELD-MASTER GORG"),
        ("Blood-Drenched Hall", "EXECUTIONER THRAX"),
        ("Grand Parapet", "BLOOD-BARON MORGATH"),
        ("Throne of Skulls", "WARLORD MORGATH")
    ]),
    ("DREAD FORTRESS", "DREAD BASTION", 0xcfd8dc, [
        ("Moat of Iron", "SIEGE-ENGINEER SKORR"),
        ("Barricade Breaker", "DREAD-GUARD VANGUARD"),
        ("Inner Ward", "DEATH-BOMB ZEALOT"),
        ("Keep of Whispers", "HEX-WARLORD NAL"),
        ("The Overlord's Keep", "DREAD-LORD VALTHOR")
    ]),
    ("FROSTBITE PEAKS", "FROST PEAKS", 0xe0f7fa, [
        ("Snowdrift Pass", "FROST-GOUGER JORM"),
        ("Frozen Waterfall", "ICE-RUNNER BLITZ"),
        ("Howling Blizzard", "GLACIAL BRUTE TANK"),
        ("Crevasse Ridge", "FROST-HEX SHAMAN"),
        ("The Ice Citadel", "WARLORD JORM")
    ]),
    ("STORM SPIRES", "THUNDER CRAGS", 0xe8eaf6, [
        ("Lightning Ridge", "STORM-CALLER THRAK"),
        ("Thunder Plateau", "ZEPHYR-BLADE REAVER"),
        ("Gale Vortex", "TEMPEST WYVERN CHIEF"),
        ("Volt Crags", "THUNDER-BRUTE TANK"),
        ("Apex of Storms", "STORM-OVERLORD THRAK")
    ]),
    ("ABYSSAL TRENCH", "DEEP ABYSS", 0xd1c4e9, [
        ("Chasm Descent", "ABYSS-STALKER SCOUT"),
        ("Fissure of Agony", "VOID-BOMB ZEALOT"),
        ("Black Caverns", "TRENCH-BRUTE TITAN"),
        ("Soul Furnace", "ABYSSAL HEX-MAGE"),
        ("The Sunken Trench", "ABYSSAL OVERLORD")
    ]),
    ("CURSED CATACOMBS", "CATACOMBS", 0xd7ccc8, [
        ("Crypt Entombment", "GRAVE-LORD GRAKK"),
        ("Bone Gallery", "SKELETAL-SHIELD GUARD"),
        ("Necrotic Hall", "DEATH-STALKER SHADOW"),
        ("Tomb of the Ancient", "MORTIS BRUTE TANK"),
        ("Catacomb Depths", "WARLORD GRAKK")
    ]),
    ("INFERNAL GATES", "HELLFIRE RIFT", 0xffccbc, [
        ("Molten Fissure", "HELL-RUNNER SCOUT"),
        ("Brimstone Bastion", "FIRE-BRUTE GARGON"),
        ("Pillars of Flame", "INFERNAL WYVERN CHIEF"),
        ("The Magma Gate", "PYRO-HEX WARLOCK"),
        ("Inferno Core", "INFERNO-WARLORD PYRAX")
    ]),
    ("VOID ABYSS", "NETHER REACHES", 0xd1c4e9, [
        ("Event Horizon", "VOID-SCOUT SHADOW"),
        ("Singularity Edge", "NULL-SHIELD TANK"),
        ("Dark Matter Surge", "WARP-BOMB ZEALOT"),
        ("Entropic Rift", "VOID-CHIEFTAIN MALIS"),
        ("The Void Core", "VOID-OVERLORD MALIS")
    ]),
    ("CELESTIAL BASTION", "GOLDEN PEAKS", 0xfff9c4, [
        ("Sunlit Foothills", "GOLD-CLAD REAVER"),
        ("Bastion Ramparts", "AEGIS SHIELD-GUARD"),
        ("Hall of Valor", "SOLAR-BRUTE TITAN"),
        ("Citadel Spires", "AURORA-HEX SHAMAN"),
        ("Bastion Apex", "WARLORD SANGUINOR")
    ]),
    ("TITAN’S CRADLE", "COLOSSUS CRATER", 0xd7ccc8, [
        ("Colossus Footprint", "TITAN-SPAWN SCOUT"),
        ("Quarry of Titans", "COLOSSUS BRUTE TITAN"),
        ("Anvil of Earth", "EARTH-SHIELD PHALANX"),
        ("Meteor Crater", "TITAN-BREAKER GORK"),
        ("Cradle Summit", "TITAN-OVERLORD GORK")
    ]),
    ("DOOM VAULT", "VAULT OF DREAD", 0xcfd8dc, [
        ("Vault Seal", "DOOM-GUARD VANGUARD"),
        ("Chamber of Ruin", "EXTINCTION BOMB-LORD"),
        ("Hall of Chains", "DREAD-STALKER ASSASSIN"),
        ("Iron Sarcophagus", "DOOM-BRUTE TITAN"),
        ("Sanctum of Doom", "DOOM-LORD MALAKAI")
    ]),
    ("REALM OF OBLIVION", "OBLIVION THRONE", 0xede7f6, [
        ("Oblivion Gates", "OBLIVION VANGUARD"),
        ("Nexus of Agony", "CHAOS-WYVERN REAVER"),
        ("Shadow of Fate", "VOID-WALKER TITAN"),
        ("Penultimate Stand", "WARLORD OF RUIN"),
        ("The Final Siege", "MALKORATH · THE OBLIVION OVERLORD")
    ])
]

# We want 100 levels. 20 chapters * 5 levels = 100 levels exactly!
levels = []
level_id = 1

for chap_idx, (chap_name, area, tint, sub_levels) in enumerate(chapters):
    for sub_idx, (lvl_name, boss_name) in enumerate(sub_levels):
        # Progress metrics:
        # scale from 0.0 (lvl 1) to 1.0 (lvl 100)
        p = (level_id - 1) / 99.0
        
        # Reward increases smoothly from 180 to 2200
        reward = int(180 + p * 1850 + sub_idx * 25)
        
        # Determine wave compositions based on level theme and level_id:
        # Wave 1: Scout / Blitz
        # Wave 2: Shield Phalanx / Heavy Line
        # Wave 3: Chaos / Infiltration (bombers, shadow, fast runners)
        # Wave 4: Heavy Vanguard / Siege (brutes, drakes, shamans)
        # Wave 5: BOSS ENCOUNTER (boss at spawnIndex 0 or 1, accompanied by thematic elites!)

        # Base counts scale gently with progression:
        # Early levels: 5-8 enemies per wave
        # Mid levels: 8-12 enemies per wave
        # Late levels: 12-16 enemies per wave
        count_base = int(5 + p * 8)
        
        # Wave 1: Scout Rush
        w1_enemies = []
        if level_id <= 10:
            w1_enemies = ['runner', 'grunt'] * (count_base // 2) + ['runner']
        elif level_id <= 30:
            w1_enemies = ['runner', 'archer', 'runner', 'grunt'] * max(1, count_base // 4)
        elif level_id <= 60:
            w1_enemies = ['shadow', 'runner', 'bomber', 'archer'] * max(1, count_base // 4)
        else:
            w1_enemies = ['shadow', 'runner', 'shadow', 'bomber', 'runner'] * max(1, count_base // 5)
        w1_interval = round(max(0.65, 1.25 - p * 0.45), 2)

        # Wave 2: Shield Phalanx / Reinforced Line
        w2_enemies = []
        if level_id <= 15:
            w2_enemies = ['shield', 'archer', 'grunt', 'shield', 'runner'] * max(1, count_base // 5)
        elif level_id <= 40:
            w2_enemies = ['shield', 'bomber', 'archer', 'shield', 'runner', 'grunt'] * max(1, count_base // 6)
        elif level_id <= 70:
            w2_enemies = ['shield', 'shaman', 'archer', 'shield', 'bomber', 'shadow'] * max(1, count_base // 6)
        else:
            w2_enemies = ['shield', 'brute', 'shaman', 'shield', 'shadow', 'bomber'] * max(1, count_base // 6)
        w2_interval = round(max(0.70, 1.30 - p * 0.45), 2)

        # Wave 3: Chaos Infiltration / Bomb Surge
        w3_enemies = []
        if level_id <= 10:
            w3_enemies = ['runner', 'grunt', 'archer', 'runner', 'shield'] * max(1, count_base // 5)
        elif level_id <= 30:
            w3_enemies = ['bomber', 'runner', 'bomber', 'archer', 'shield'] * max(1, count_base // 5)
        elif level_id <= 60:
            w3_enemies = ['shadow', 'bomber', 'shaman', 'bomber', 'shadow', 'runner'] * max(1, count_base // 6)
        else:
            w3_enemies = ['shadow', 'bomber', 'drakerider', 'bomber', 'shadow', 'shaman'] * max(1, count_base // 6)
        w3_interval = round(max(0.60, 1.15 - p * 0.45), 2)

        # Wave 4: Siege Engine & Aerial Wing
        w4_enemies = []
        if level_id <= 20:
            w4_enemies = ['shield', 'shaman', 'grunt', 'archer', 'shield', 'runner'] * max(1, count_base // 6)
        elif level_id <= 40:
            w4_enemies = ['brute', 'archer', 'shaman', 'bomber', 'runner', 'shield'] * max(1, count_base // 6)
        elif level_id <= 70:
            w4_enemies = ['drakerider', 'brute', 'shaman', 'drakerider', 'shadow', 'shield'] * max(1, count_base // 6)
        else:
            w4_enemies = ['drakerider', 'brute', 'warlord', 'shaman', 'shadow', 'drakerider'] * max(1, count_base // 6)
        w4_interval = round(max(0.75, 1.35 - p * 0.45), 2)

        # Wave 5: BOSS ASSAULT!
        # Remember: simulation.ts triggers boss at isBossWave && spawnIndex === 1!
        # So enemy at index 1 is the BOSS!
        # Index 0 is a vanguard herald (grunt, runner, or shield).
        # Index 1 is the designated boss enemy!
        # Following indices are the elite guard!
        boss_kind = 'chief' if level_id <= 25 else 'warlord' if level_id <= 50 else 'chief' if level_id % 2 == 1 else 'warlord'
        
        # Vanguard herald:
        herald = 'runner' if level_id <= 20 else 'shield' if level_id <= 60 else 'shadow'
        
        # Elite escort:
        escort = []
        if level_id <= 15:
            escort = ['shield', 'archer', 'grunt', 'runner'] * max(1, count_base // 4)
        elif level_id <= 35:
            escort = ['shield', 'bomber', 'shaman', 'brute', 'archer'] * max(1, count_base // 5)
        elif level_id <= 65:
            escort = ['brute', 'drakerider', 'shaman', 'shield', 'shadow'] * max(1, count_base // 5)
        else:
            escort = ['brute', 'warlord' if boss_kind == 'chief' else 'chief', 'drakerider', 'shaman', 'shadow', 'bomber'] * max(1, count_base // 6)
        
        w5_enemies = [herald, boss_kind] + escort
        w5_interval = round(max(0.85, 1.45 - p * 0.45), 2)

        lvl_obj = {
            "id": level_id,
            "name": lvl_name,
            "area": area,
            "subtitle": f"Stage {level_id} · {boss_name}",
            "tint": tint,
            "reward": reward,
            "boss": boss_name,
            "waves": [
                {"enemies": w1_enemies, "interval": w1_interval},
                {"enemies": w2_enemies, "interval": w2_interval},
                {"enemies": w3_enemies, "interval": w3_interval},
                {"enemies": w4_enemies, "interval": w4_interval},
                {"enemies": w5_enemies, "interval": w5_interval}
            ]
        }
        levels.append(lvl_obj)
        level_id += 1

print(f"Generated {len(levels)} levels across {len(chapters)} chapters!")
print(f"Level 1 waves sample: {[len(w['enemies']) for w in levels[0]['waves']]}")
print(f"Level 50 waves sample: {[len(w['enemies']) for w in levels[49]['waves']]}")
print(f"Level 100 waves sample: {[len(w['enemies']) for w in levels[99]['waves']]}")

# Save to temporary json to inspect or inject
with open("Fortress-Rush-10-Levels/new_levels.json", "w", encoding="utf-8") as f:
    json.dump(levels, f, indent=1)
print("Saved new_levels.json successfully!")
