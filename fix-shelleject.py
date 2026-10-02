path = r"d:\New folder (55)\Fortress-Rush-10-Levels\source\src\main.ts"
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find exact lines with shellEject
for i, line in enumerate(lines, 1):
    if 'shellEject' in line:
        print(f"Line {i}: repr={repr(line[:80])}")

# Line 66 is the duplicate - remove it
new_lines = []
found_first_shell = False
for i, line in enumerate(lines, 1):
    if "if(e.type==='shoot'){if(Math.random()<0.45)audio.play('shellEject');}" in line:
        if not found_first_shell:
            found_first_shell = True
            print(f"Removing duplicate line {i}")
            continue  # Skip this line
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

# Verify
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()
count = c.count('shellEject')
print(f"shellEject occurrences after fix: {count} (should be 1)")
