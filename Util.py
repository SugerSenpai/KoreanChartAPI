import json

def prettifyDictionary(dict):
    jsonString = json.dumps(dict, ensure_ascii=False, indent = 4)
    return jsonString

# Example: print(prettifyDictionary(getSongByRank(getRanking(), 5)))
def getSongByRank(dict, rank):
    return dict[rank]

def getSongTitle(dict, rank):
    return dict[rank]['title']

def getSongArtist(dict, rank):
    return dict[rank]['artist']

def getSongAlbum(dict, rank):
    return dict[rank]['album']