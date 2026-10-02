import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

css_path = r"Fortress-Rush-10-Levels\source\src\style.css"
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

old_brand = ".brand{position:absolute;width:63%;height:26%;top:9.8%;left:18.5%;filter:drop-shadow(0 6px 3px #26351855)}"
new_brand = ".brand{position:absolute;width:56%;max-width:245px;top:5.8%;left:50%;transform:translateX(-50%);filter:drop-shadow(0 6px 4px #1b2612aa);pointer-events:none}"

old_ribbon = ".home-ribbon{position:absolute;top:36%;width:100%;text-align:center;text-shadow:0 2px 3px #29371d}"
new_ribbon = ".home-ribbon{position:absolute;top:24.2%;width:100%;text-align:center;text-shadow:0 2px 3px #29371d;pointer-events:none}"

if old_brand in css:
    css = css.replace(old_brand, new_brand, 1)
    print("1. Moved brand logo up to top: 5.8% and centered it")
else:
    print("1. WARNING: old_brand not found")

if old_ribbon in css:
    css = css.replace(old_ribbon, new_ribbon, 1)
    print("2. Moved home-ribbon up to top: 24.2%")
else:
    print("2. WARNING: old_ribbon not found")

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css successfully!")
