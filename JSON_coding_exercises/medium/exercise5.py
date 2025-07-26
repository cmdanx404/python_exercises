import json

student = {
    "name": "Maria",
    "grades": {
        "math": 85,
        "science": 92
    },
    "enrolled": True
}

json_str = json.dumps(student, indent=4)
print(json_str)
