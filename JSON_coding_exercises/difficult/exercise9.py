import json

json_data = '{"id": 1, "name": "Elise"}'
data = json.loads(json_data)

required = ["id", "name", "email"]
missing = [key for key in required if key not in data]

if not missing:
    print("Valid JSON: all required keys present.")
else:
    print("Missing keys:", missing)
