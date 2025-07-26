import json

users_json = '''
[
  {"name": "Liam", "age": 17},
  {"name": "Emma", "age": 22},
  {"name": "Noah", "age": 19}
]
'''

users = json.loads(users_json)

for user in users:
    if user["age"] > 18:
        print(user["name"])
