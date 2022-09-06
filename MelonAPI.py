from codecs import ascii_encode
from bs4 import BeautifulSoup
import requests as r
import json as js

url = "https://www.melon.com/chart/index.htm"

html = r.get(url, headers={"User-Agent": "XY"})
doc = BeautifulSoup(html.text, "html.parser")

result = doc("tr", attrs={"data-song-no": True})

ranking = {}
rank = 1
for tag in result:
    ranking[rank] = {
        "title": tag.find(class_="ellipsis rank01").text.replace('\n', ''),
        "artist": tag.find,
        "album": tag.find,
        "rank": tag.find(class_="rank").text,
    }
    rank += 1

jsonString = js.dumps(ranking, ensure_ascii=False, indent = 4)
print(jsonString)