import os
from PIL import Image

src = r'C:\Users\Anmol\.gemini\antigravity\brain\7508c5b6-1323-47ed-83a7-dc374822e519\arena_clean_bg_1790844525567.jpg'
im = Image.open(src).resize((768, 1152), Image.Resampling.LANCZOS)

dests = [
    r'Fortress-Rush-10-Levels\source\public\assets\background.webp',
    r'Fortress-Rush-10-Levels\source\public\assets\background-clean.webp',
    r'Fortress-Rush-10-Levels\web-build\assets\background.webp',
    r'Fortress-Rush-10-Levels\web-build\assets\background-clean.webp'
]

for d in dests:
    im.save(d, 'WEBP', quality=92)
    print(f"Saved clean arena background to {d} (size: {os.path.getsize(d)} bytes)")
