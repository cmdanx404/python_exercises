import json

with open("data.json", "r") as f:
    data = json.load(f)

for key, value in data.items():
    print(f"{key}: {value}")
