import json

with open("users1.json", "r") as f1:
    users1 = json.load(f1)

with open("users2.json", "r") as f2:
    users2 = json.load(f2)

merged = {**users1, **users2}

with open("merged_users.json", "w") as f:
    json.dump(merged, f, indent=4)
