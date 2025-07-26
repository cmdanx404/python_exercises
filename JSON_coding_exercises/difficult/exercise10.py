import json
import csv

users_json = '''
[
  {"name": "Anne", "age": 24},
  {"name": "Mark", "age": 31}
]
'''

users = json.loads(users_json)

with open("users.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["name", "age"])
    writer.writeheader()
    for user in users:
        writer.writerow(user)
