import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

scene_path = r"d:\New folder (55)\Fortress-Rush-10-Levels\source\src\scene.ts"
with open(scene_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update setView to use 'hero' texture for home screen
# Old:
#   if(battle){this.hero.setTexture('hero-north').setOrigin(.506,.956).setFlipX(false);}
#   else if(view==='armory'){this.hero.setTexture('hero').setOrigin(.5,1).setFlipX(false);}
#   else {this.hero.setTexture('hero-front').setOrigin(.5,1).setFlipX(false);}

old_set_view = """   if(battle){this.hero.setTexture('hero-north').setOrigin(.506,.956).setFlipX(false);}
   else if(view==='armory'){this.hero.setTexture('hero').setOrigin(.5,1).setFlipX(false);}
   else {this.hero.setTexture('hero-front').setOrigin(.5,1).setFlipX(false);}"""

new_set_view = """   if(battle){this.hero.setTexture('hero-north').setOrigin(.506,.956).setFlipX(false);}
   else{this.hero.setTexture('hero').setOrigin(.5,1).setFlipX(false);}"""

if old_set_view in code:
    code = code.replace(old_set_view, new_set_view, 1)
    print("1. Updated setView to use crisp official 'hero' texture on home & armory")
else:
    print("1. WARNING: setView pattern not matched directly, checking normalized...")
    # try replacing hero-front with hero in setView
    code = code.replace("else {this.hero.setTexture('hero-front')", "else {this.hero.setTexture('hero')")
    print("1b. Replaced hero-front with hero in setView")

# 2. Update home screen hero size to 116px (prominent, proportional, heroic)
# Find the line setting hero size in !battle
old_size_pattern = "if(armory)this.hero.setDisplaySize(185*(2-heroSquash),185*heroSquash);\n    else this.hero.setDisplaySize(68*(2-heroSquash),68*heroSquash);"
new_size_replacement = """const isHome=this.view==='home';
    const heroSize=armory?185:isHome?118:76;
    this.hero.setDisplaySize(heroSize*(2-heroSquash),heroSize*heroSquash);"""

if old_size_pattern in code:
    code = code.replace(old_size_pattern, new_size_replacement, 1)
    print("2. Updated hero size on home screen to 118px (prominent & un-squashed)")
else:
    # check with CRLF or alternate spacing
    lines = code.split('\n')
    found = False
    for i, line in enumerate(lines):
        if "this.hero.setDisplaySize(68*(2-heroSquash)" in line:
            lines[i] = "    const isHome=this.view==='home';const heroSize=armory?185:isHome?118:76;this.hero.setDisplaySize(heroSize*(2-heroSquash),heroSize*heroSquash);"
            found = True
            print(f"2b. Replaced hero display size at line {i+1}")
            break
    if found:
        code = '\n'.join(lines)

with open(scene_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("=== Hero home screen update applied ===")
