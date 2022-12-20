import json

def pretty_print(obj):
    return json.dumps(obj, indent=4, sort_keys=True)
