import json


def capitalize(file):
    with open(file, 'r', encoding='utf-8') as f:
        new_dict = {}
        content = json.load(f)
        for key, value in content.items():
            key = key.capitalize()
            value = value
            new_dict[key] = value
        return new_dict

print(capitalize('data.json'))