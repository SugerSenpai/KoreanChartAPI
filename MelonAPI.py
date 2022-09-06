from bs4 import BeautifulSoup
import requests as r
import json as js

url = "https://www.melon.com/chart/index.htm"

html = r.get(url, headers={"User-Agent": "XY"})

def prettifyDictionary(dict):
    jsonString = js.dumps(dict, ensure_ascii=False, indent = 4)
    return jsonString

def getRanking():
    doc = BeautifulSoup(html.text, "html.parser")
    allTags = doc("tr", attrs={"data-song-no": True})
    ranking = {}
    rank = 1
    for tag in allTags:
        ranking[rank] = {
            "title": tag.find(class_="ellipsis rank01").text.replace('\n', ''),
            "artist": tag.find(class_="checkEllipsis").text.replace('\n', ''),
            "album": tag.find(class_="ellipsis rank03").text.replace('\n', ''),
            "rank": rank,
        }
        rank += 1
    return ranking

result = getRanking()
print(prettifyDictionary(result))
# print(prettifyDictionary(result[15]['title']))