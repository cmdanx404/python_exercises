import json

person = {
    "name": "Alice",
    "age": 30,
    "city": "Manila"
}

json_str = json.dumps(person)
print(json_str)
