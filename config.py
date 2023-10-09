import json

def load_config(config_file):
    with open(config_file, 'r') as file:
        return json.load(file)

def save_config(config, config_file):
    with open(config_file, 'w') as file:
        json.dump(config, file, indent=4)
