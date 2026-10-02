import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# 1. Patch scene.ts to use 'background-clean'
scene_path = r"Fortress-Rush-10-Levels\source\src\scene.ts"
with open(scene_path, 'r', encoding='utf-8') as f:
    scene = f.read()

scene = scene.replace("'background',", "'background','background-clean',")
scene = scene.replace("this.bg=this.add.image(210,420,'background')", "this.bg=this.add.image(210,420,'background-clean')")
scene = scene.replace("this.bg.setTexture('background').clearTint();", "this.bg.setTexture('background-clean').clearTint();")

with open(scene_path, 'w', encoding='utf-8') as f:
    f.write(scene)
print("1. Updated scene.ts to use background-clean texture key")

# 2. Patch assets.ts with cache buster query string
assets_path = r"Fortress-Rush-10-Levels\source\src\assets.ts"
with open(assets_path, 'r', encoding='utf-8') as f:
    assets = f.read()

old_assets = "return typeof __FORTRESS_ASSETS__ === 'undefined'\n    ? `/assets/${name}.webp`\n    : __FORTRESS_ASSETS__[name];"
new_assets = "return typeof __FORTRESS_ASSETS__ === 'undefined'\n    ? `/assets/${name}.webp?v=102`\n    : __FORTRESS_ASSETS__[name];"

if old_assets in assets:
    assets = assets.replace(old_assets, new_assets, 1)
    print("2. Added cache buster ?v=102 in assets.ts")
else:
    # try replacing `/assets/${name}.webp`
    assets = assets.replace("`/assets/${name}.webp`", "`/assets/${name}.webp?v=102`")
    print("2b. Replaced with cache buster in assets.ts")

with open(assets_path, 'w', encoding='utf-8') as f:
    f.write(assets)

# 3. Patch style.css to place brand logo and ribbon higher up and nicely proportioned
css_path = r"Fortress-Rush-10-Levels\source\src\style.css"
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace any existing .brand and .home-ribbon
import re
css = re.sub(
    r'\.brand\{[^}]*\}',
    '.brand{position:absolute;width:48%;max-width:215px;top:7.2%;left:50%;transform:translateX(-50%);filter:drop-shadow(0 6px 4px #1b2612bb);pointer-events:none;z-index:2}',
    css
)
css = re.sub(
    r'\.home-ribbon\{[^}]*\}',
    '.home-ribbon{position:absolute;top:23.2%;width:100%;text-align:center;text-shadow:0 2px 3px #29371d;pointer-events:none;z-index:2}',
    css
)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("3. Repositioned title logo to top: 7.2% and ribbon to top: 23.2% in style.css")

# 4. Make sure background.webp is also replaced with clean background
from PIL import Image
src = r'C:\Users\Anmol\.gemini\antigravity\brain\7508c5b6-1323-47ed-83a7-dc374822e519\clean_kingdom_bg_1790842031913.jpg'
im = Image.open(src).resize((768, 1152), Image.Resampling.LANCZOS)
for dest in [
    r'Fortress-Rush-10-Levels\source\public\assets\background.webp',
    r'Fortress-Rush-10-Levels\source\public\assets\background-clean.webp',
    r'Fortress-Rush-10-Levels\web-build\assets\background.webp',
    r'Fortress-Rush-10-Levels\web-build\assets\background-clean.webp'
]:
    im.save(dest, 'WEBP', quality=90)
    print("4. Saved clean background to", dest)

print("\n=== All updates applied successfully! ===")
