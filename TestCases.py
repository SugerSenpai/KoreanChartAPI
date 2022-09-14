import json

def prettifyDictionary(dict):
    jsonString = json.dumps(dict, ensure_ascii=False, indent = 4)
    return jsonString