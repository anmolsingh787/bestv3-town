import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

scene_path = r"Fortress-Rush-10-Levels\source\src\scene.ts"
with open(scene_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update setView: only home uses hero-front facing straight! Battle keeps hero-north.
old_set = """   if(battle||home){this.hero.setTexture('hero-north').setOrigin(.506,.956).setFlipX(false);}
    else{this.hero.setTexture('hero').setOrigin(.5,1).setFlipX(false);}"""

new_set = """   if(battle){this.hero.setTexture('hero-north').setOrigin(.506,.956).setFlipX(false);}
   else if(home){this.hero.setTexture('hero-front').setOrigin(.5,.96).setFlipX(false);}
   else if(view==='armory'){this.hero.setTexture('hero').setOrigin(.5,1).setFlipX(false);}
   else{this.hero.setTexture('hero-front').setOrigin(.5,1).setFlipX(false);}"""

if old_set in code:
    code = code.replace(old_set, new_set, 1)
    print("1. Updated setView: home uses hero-front (facing straight), battle keeps hero-north")
else:
    # try lines approach
    lines = code.split('\n')
    for i, l in enumerate(lines):
        if "if(battle||home)" in l:
            lines[i] = "   if(battle){this.hero.setTexture('hero-north').setOrigin(.506,.956).setFlipX(false);}\n   else if(home){this.hero.setTexture('hero-front').setOrigin(.5,.96).setFlipX(false);}\n   else if(view==='armory'){this.hero.setTexture('hero').setOrigin(.5,1).setFlipX(false);}"
            print("1b. Replaced setView line successfully")
            break
    code = '\n'.join(lines)

# 2. Update home hero display size in update() for proper natural aspect ratio of hero-front (224x420):
old_size = "this.hero.setDisplaySize(58*(2-heroSquash),130*heroSquash);"
new_size = "this.hero.setDisplaySize(66*(2-heroSquash),124*heroSquash);"

if old_size in code:
    code = code.replace(old_size, new_size, 1)
    print("2. Updated home hero display size for hero-front natural 1.875 ratio")
else:
    print("2. Warning: old_size pattern not found")

with open(scene_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("=== scene.ts patched successfully! ===")
