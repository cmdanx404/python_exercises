import json

with open("config.json", "r") as f:
    config = json.load(f)

config["volume"] = 75

with open("config.json", "w") as f:
    json.dump(config, f, indent=4)
