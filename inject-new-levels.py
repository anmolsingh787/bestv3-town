import json

data_ts_path = r"Fortress-Rush-10-Levels\source\src\data.ts"
with open(data_ts_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Load new_levels.json
with open(r"Fortress-Rush-10-Levels\new_levels.json", "r", encoding="utf-8") as f:
    levels_data = json.load(f)

# Find start of LEVELS array
start_marker = "export const LEVELS:Level[] = ["
end_marker = "\nexport type UpgradeId ="

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print(f"Error finding markers: start_idx={start_idx}, end_idx={end_idx}")
    exit(1)

# Format levels_data as compact JSON without excessive newlines
levels_json = json.dumps(levels_data, indent=1)

new_text = text[:start_idx] + f"export const LEVELS:Level[] = {levels_json};\n" + text[end_idx:]

with open(data_ts_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print(f"Successfully injected 100 new varied levels into {data_ts_path}!")
