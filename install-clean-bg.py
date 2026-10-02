import os
from PIL import Image

src_img = r'C:\Users\Anmol\.gemini\antigravity\brain\7508c5b6-1323-47ed-83a7-dc374822e519\clean_kingdom_bg_1790842031913.jpg'
dest_webp = r'Fortress-Rush-10-Levels\source\public\assets\background.webp'
backup_webp = r'Fortress-Rush-10-Levels\source\public\assets\background_goblin_old.webp'

if os.path.exists(dest_webp) and not os.path.exists(backup_webp):
    os.rename(dest_webp, backup_webp)
    print("Backed up old background to", backup_webp)

im = Image.open(src_img)
# Resize to 768x1152 using high quality Lanczos filter
im_resized = im.resize((768, 1152), Image.Resampling.LANCZOS)
im_resized.save(dest_webp, 'WEBP', quality=88)
print(f"Saved new clean background to {dest_webp} (size: {os.path.getsize(dest_webp)} bytes)")
