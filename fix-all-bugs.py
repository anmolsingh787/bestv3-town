import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def fix_file(path, fixes):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    applied = []
    for old, new, label in fixes:
        if old in content:
            content = content.replace(old, new, 1)
            applied.append(label)
            print(f"  OK: {label}")
        else:
            print(f"  SKIP: {label}")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return applied

main_path = r"d:\New folder (55)\Fortress-Rush-10-Levels\source\src\main.ts"
sim_path  = r"d:\New folder (55)\Fortress-Rush-10-Levels\source\src\simulation.ts"
scene_path = r"d:\New folder (55)\Fortress-Rush-10-Levels\source\src\scene.ts"
audio_path = r"d:\New folder (55)\Fortress-Rush-10-Levels\source\src\audio.ts"

print("\n=== main.ts fixes ===")
fixes_main = [
    (
        "if(['collect','towerHit','shieldBlock','slash','magicHeal','dragonBreath','arrowHit','magicExplode','bladeHit'].includes(e.type))audio.play(e.type);",
        "if(['hit','collect','towerHit','shieldBlock','slash','magicHeal','dragonBreath','arrowHit','magicExplode','bladeHit'].includes(e.type))audio.play(e.type);",
        "Add hit to audio events"
    ),
    (
        "if(e.type==='boss'||e.type==='bossSpawn'){audio.play('bossRoar');toast(`\u2757\uFE0F BOSS INCOMING \u00B7 ${e.kind||'WAR CHIEF'}`,3200);}",
        "if(e.type==='bossSpawn'){audio.play('bossRoar');toast(`\u2757\uFE0F BOSS INCOMING \u00B7 ${e.kind||'WAR CHIEF'}`,3200);}",
        "Fix double bossRoar"
    ),
    (
        "if(e.key.toLowerCase()==='r'){if(!sim.repair())sim.startReload();}",
        "if(e.key.toLowerCase()==='r'){if(sim.repair())audio.play('upgrade');else sim.startReload();}",
        "Add R-key repair audio"
    ),
    (
        "toast(target.textContent?.match(/(?:Heavy Rounds|Rapid Fire|Twin Shot|Piercing Ammo|Blast Rounds|Side Cannon|Iron Walls|Field Medic|Frost Rounds|Thunder Strike|Inferno Meteor|Toxic Spores|Energy Aegis|Tri-Shot Burst|Auto-Fire Gatling)/)?.[0]+' equipped')",
        "toast((sim.choices.find(u=>u.id===target.dataset.upgrade)?.name||'Power')+' equipped')",
        "Fix undefined equipped toast"
    ),
    (
        "setText('helper-l-status','ACTIVE [Q]')",
        "setText('helper-l-status','ACTIVE')",
        "Remove misleading Q from active helper"
    ),
    (
        "setText('helper-r-status','ACTIVE [E]')",
        "setText('helper-r-status','ACTIVE')",
        "Remove misleading E from active helper"
    ),
]
fix_file(main_path, fixes_main)

print("\n=== simulation.ts fixes ===")
fixes_sim = [
    (
        "const dx=e.x-p.x,dy=e.y-ENEMIES[e.kind].size*.3-p.y,dist=Math.hypot(dx,dy);",
        "const dx=e.x-p.x,dy=e.y-ENEMIES[e.kind].size*.3-p.y,dist=Math.hypot(dx,dy)||1;",
        "Fix div-by-zero in projectile homing"
    ),
    (
        "private hostile(e:Enemy){if(this.shots.length>=100)return;const dx=this.x-e.x,dy=660-(e.y-25),d=Math.hypot(dx,dy);",
        "private hostile(e:Enemy){if(this.shots.length>=100)return;const dx=this.x-e.x,dy=660-(e.y-25),d=Math.hypot(dx,dy)||1;",
        "Fix div-by-zero in hostile()"
    ),
    (
        "const pts=e.kind==='chief'?80:e.kind==='warlord'?60:e.kind==='drakerider'?35:e.kind==='brute'?30:e.kind==='shaman'?25:e.kind==='shield'?20:e.kind==='bomber'?20:e.kind==='archer'?15:e.kind==='runner'?12:10;",
        "const pts=e.kind==='chief'?80:e.kind==='warlord'?60:e.kind==='drakerider'?35:e.kind==='brute'?30:e.kind==='shaman'?25:e.kind==='shadow'?25:e.kind==='shield'?20:e.kind==='bomber'?20:e.kind==='archer'?15:e.kind==='runner'?12:10;",
        "Fix shadow getting only 10 battle points"
    ),
    (
        "if(isBossEnemy||kind==='chief'){enemy.lane=0;this.event('boss',{kind:this.level.boss,x:210,y:165});}",
        "if(isBossEnemy){enemy.lane=0;this.event('boss',{kind:this.level.boss,x:210,y:165});}else if(kind==='chief'){enemy.lane=0;}",
        "Fix false boss announcement for chief in non-boss waves"
    ),
]
fix_file(sim_path, fixes_sim)

print("\n=== scene.ts fixes ===")
fixes_scene = [
    (
        "if(hasLeft)this.helperLeftSprite.setTexture('helper-'+this.save.helperLeft);",
        "if(hasLeft)this.helperLeftSprite.setTexture(this.save.helperLeft==='blade'?'helper-swordsman':'helper-'+this.save.helperLeft);",
        "Fix blade texture (left menu)"
    ),
    (
        "if(hasRight)this.helperRightSprite.setTexture('helper-'+this.save.helperRight);",
        "if(hasRight)this.helperRightSprite.setTexture(this.save.helperRight==='blade'?'helper-swordsman':'helper-'+this.save.helperRight);",
        "Fix blade texture (right menu)"
    ),
    (
        "this.helperLeftSprite.setTexture(`helper-${this.save.helperLeft}-north`)",
        "this.helperLeftSprite.setTexture(this.save.helperLeft==='blade'?'helper-swordsman-north':`helper-${this.save.helperLeft}-north`)",
        "Fix blade north texture (left battle)"
    ),
    (
        "this.helperRightSprite.setTexture(`helper-${this.save.helperRight}-north`)",
        "this.helperRightSprite.setTexture(this.save.helperRight==='blade'?'helper-swordsman-north':`helper-${this.save.helperRight}-north`)",
        "Fix blade north texture (right battle)"
    ),
]
fix_file(scene_path, fixes_scene)

print("\n=== audio.ts fixes ===")
fixes_audio = [
    (
        "  tone(frequency: number, duration = 0.12, type: OscillatorType = 'sine', volume = 0.035, end?: number) {\n    if (!this.ctx || !this.enabled) return;",
        "  tone(frequency: number, duration = 0.12, type: OscillatorType = 'sine', volume = 0.035, end?: number, forcePlay = false) {\n    if (!this.ctx || (!this.enabled && !forcePlay)) return;",
        "Fix music muted when SFX disabled"
    ),
    (
        "      if (n) this.tone(n, 0.48, 'sine', 0.008);",
        "      if (n) this.tone(n, 0.48, 'sine', 0.008, undefined, true);",
        "Music uses forcePlay"
    ),
    (
        "    o.frequency.setValueAtTime(frequency, t);",
        "    o.frequency.setValueAtTime(Math.max(1, frequency), t);",
        "Guard frequency <= 0"
    ),
    (
        "  play(name: string) {\n    if (!this.ctx) return;",
        "  play(name: string) {\n    if (!this.ctx || !this.enabled) return;",
        "Add enabled check in play()"
    ),
]
fix_file(audio_path, fixes_audio)

print("\n=== ALL FIXES COMPLETE ===")
