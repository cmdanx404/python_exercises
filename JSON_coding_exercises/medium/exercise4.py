import json

data = {
    "id": 101,
    "title": "Learn Python",
    "is_completed": False
}

with open("task.json", "w") as f:
    json.dump(data, f, indent=4)
