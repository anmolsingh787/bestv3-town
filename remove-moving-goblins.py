import os, sys, io
from PIL import Image

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# 1. Prepare bg-arena-v3 from arena_clean_bg_1790844525567.jpg
src = r'C:\Users\Anmol\.gemini\antigravity\brain\7508c5b6-1323-47ed-83a7-dc374822e519\arena_clean_bg_1790844525567.jpg'
im = Image.open(src).resize((768, 1152), Image.Resampling.LANCZOS)

target_files = [
    r'Fortress-Rush-10-Levels\source\public\assets\bg-arena-v3.webp',
    r'Fortress-Rush-10-Levels\source\public\assets\background.webp',
    r'Fortress-Rush-10-Levels\source\public\assets\background-clean.webp',
    r'Fortress-Rush-10-Levels\source\dist\assets\bg-arena-v3.webp',
    r'Fortress-Rush-10-Levels\source\dist\assets\background.webp',
    r'Fortress-Rush-10-Levels\source\dist\assets\background-clean.webp',
    r'Fortress-Rush-10-Levels\web-build\assets\bg-arena-v3.webp',
    r'Fortress-Rush-10-Levels\web-build\assets\background.webp',
    r'Fortress-Rush-10-Levels\web-build\assets\background-clean.webp',
]

for t in target_files:
    os.makedirs(os.path.dirname(t), exist_ok=True)
    im.save(t, 'WEBP', quality=92)
    print("Saved clean arena background to", t)

# 2. Update scene.ts:
# Remove this.dummy completely from the scene!
# And use 'bg-arena-v3' texture!
scene_path = r'Fortress-Rush-10-Levels\source\src\scene.ts'
with open(scene_path, 'r', encoding='utf-8') as f:
    scene = f.read()

# Add bg-arena-v3 to textureNames
scene = scene.replace("'background-clean',", "'background-clean','bg-arena-v3',")

# Update initial bg and setView bg
scene = scene.replace("'background-clean'", "'bg-arena-v3'")

# REMOVE this.dummy creation from create():
# Line 35: for(let i=0;i<3;i++){const d=this.add.image(160+i*52,280+i*20,i===2?'shield':'grunt').setOrigin(.5,1).setDisplaySize(33,39).setDepth(290+i);this.dummy.push(d);}
dummy_create = "for(let i=0;i<3;i++){const d=this.add.image(160+i*52,280+i*20,i===2?'shield':'grunt').setOrigin(.5,1).setDisplaySize(33,39).setDepth(290+i);this.dummy.push(d);}"
if dummy_create in scene:
    scene = scene.replace(dummy_create, "// Dummies removed per user request")
    print("2. Removed dummy goblin creation from scene.ts")

# Make sure dummy is never visible
scene = scene.replace("this.dummy.forEach(d=>d.setVisible(home));", "this.dummy.forEach(d=>d.setVisible(false));")

# Remove dummy animation in non-battle update
old_dummy_anim = """   this.dummy.forEach((d,i)=>{
    const spring=Math.sin(time*.005+i*1.8)*5;
    d.y=300+i*12+Math.abs(spring)*0.6;
    d.angle=spring;
    d.setScale(1+spring*0.015,1-spring*0.015);
    if(Math.random()<0.03)this.puff(d.x,d.y-18,0x8d6e63,2.2);
   });"""

if old_dummy_anim in scene:
    scene = scene.replace(old_dummy_anim, "// Dummy animations removed")
    print("3. Removed dummy animations from scene.ts")

with open(scene_path, 'w', encoding='utf-8') as f:
    f.write(scene)

# 3. Update assets.ts with new version query
assets_path = r'Fortress-Rush-10-Levels\source\src\assets.ts'
with open(assets_path, 'r', encoding='utf-8') as f:
    assets = f.read()

assets = assets.replace("?v=102", "?v=103")
with open(assets_path, 'w', encoding='utf-8') as f:
    f.write(assets)
print("4. Bumped cache buster to ?v=103 in assets.ts")

print("=== Done patching! ===")
