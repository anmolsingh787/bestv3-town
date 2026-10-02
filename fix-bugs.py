import re

# Fix 1: Remove duplicate shellEject in main.ts (line 66)
path = r"d:\New folder (55)\Fortress-Rush-10-Levels\source\src\main.ts"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# The duplicate line that causes double shellEject
old = "  if(e.type==='shoot'){if(Math.random()<0.45)audio.play('shellEject');}\r\n"
if old in content:
    content = content.replace(old, '', 1)
    print("FIX 1: Removed duplicate shellEject line from main.ts")
else:
    # Try without \r\n
    old2 = "  if(e.type==='shoot'){if(Math.random()<0.45)audio.play('shellEject');}\n"
    if old2 in content:
        content = content.replace(old2, '', 1)
        print("FIX 1: Removed duplicate shellEject line from main.ts (LF)")
    else:
        print("FIX 1: SKIP - duplicate shellEject line not found (maybe already fixed)")
        # Debug: find shellEject occurrences
        for i, line in enumerate(content.split('\n'), 1):
            if 'shellEject' in line:
                print(f"  Line {i}: {line.strip()}")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()
count = c.count('shellEject')
print(f"  shellEject occurrences after fix: {count}")

# Fix 2: Check simulation.ts - verify autofire guard against no enemies
sim_path = r"d:\New folder (55)\Fortress-Rush-10-Levels\source\src\simulation.ts"
with open(sim_path, 'r', encoding='utf-8') as f:
    sim = f.read()

# Check if autofire has proper guard
if 'if(autoTarget)this.shootTarget(autoTarget)' in sim:
    print("FIX 2: autofire has proper null guard (OK)")
else:
    print("FIX 2: WARNING - autofire guard not found, checking...")
    for i, line in enumerate(sim.split('\n'), 1):
        if 'autofire' in line.lower() and 'autoTarget' in line:
            print(f"  Line {i}: {line.strip()}")

# Fix 3: Verify boss spawn - isBossEnemy checks
boss_spawn_count = sim.count('isBossEnemy')
print(f"FIX 3: isBossEnemy references: {boss_spawn_count}")

# Fix 4: Check if deployLeft/Right deducts battlePoints
if 'this.battlePoints-=' in sim or 'battlePoints-=' in sim:
    print("FIX 4: battlePoints deduction found (OK)")
else:
    print("FIX 4: BUG FOUND - deployLeft/Right never deducts battlePoints!")
    # Fix it: add battlePoints deduction
    old_deploy_left = "deployLeft():boolean{if(!this.canDeployLeft())return false;this.helperLeftUnlocked=true;"
    new_deploy_left = "deployLeft():boolean{if(!this.canDeployLeft())return false;this.battlePoints-=this.leftDeployCost;this.helperLeftUnlocked=true;"
    old_deploy_right = "deployRight():boolean{if(!this.canDeployRight())return false;this.helperRightUnlocked=true;"
    new_deploy_right = "deployRight():boolean{if(!this.canDeployRight())return false;this.battlePoints-=this.rightDeployCost;this.helperRightUnlocked=true;"
    
    sim = sim.replace(old_deploy_left, new_deploy_left)
    sim = sim.replace(old_deploy_right, new_deploy_right)
    
    with open(sim_path, 'w', encoding='utf-8') as f:
        f.write(sim)
    print("  FIXED: Added battlePoints deduction to deployLeft/deployRight")

# Verify fix
with open(sim_path, 'r', encoding='utf-8') as f:
    sim_check = f.read()
bp_deduct = sim_check.count('battlePoints-=')
print(f"  battlePoints-= count: {bp_deduct}")

print("\n=== All fixes applied ===")
