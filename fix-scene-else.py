import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

scene_path = r"Fortress-Rush-10-Levels\source\src\scene.ts"
with open(scene_path, 'r', encoding='utf-8') as f:
    code = f.read()

bad_str = """   if(battle||home){this.hero.setTexture('hero-north').setOrigin(.506,.956).setFlipX(false);}
    else{this.hero.setTexture('hero').setOrigin(.5,1).setFlipX(false);}
   else {this.hero.setTexture('hero').setOrigin(.5,1).setFlipX(false);}"""

good_str = """   if(battle||home){this.hero.setTexture('hero-north').setOrigin(.506,.956).setFlipX(false);}
   else{this.hero.setTexture('hero').setOrigin(.5,1).setFlipX(false);}"""

if bad_str in code:
    code = code.replace(bad_str, good_str, 1)
    print("Fixed double else statement in scene.ts")
else:
    # try lines replacement
    lines = code.split('\n')
    for i in range(len(lines)-2):
        if "if(battle||home)" in lines[i] and "else{" in lines[i+1] and "else {" in lines[i+2]:
            lines.pop(i+2)
            code = '\n'.join(lines)
            print("Removed redundant else line")
            break

with open(scene_path, 'w', encoding='utf-8') as f:
    f.write(code)
