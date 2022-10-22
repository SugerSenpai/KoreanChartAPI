from bs4 import BeautifulSoup
from TestCases import prettifyDictionary
import requests as r

url = "https://m.bugs.co.kr/chart"

html = r.get(url, headers={"User-Agent": "XY"})


def getRanking():
    doc = BeautifulSoup(html.text, "html.parser")
    allTags = doc.find_all(class_="trackInfo")
    ranking = {}
    rank = 1
    for tag in allTags:
        ranking[rank] = {
            "title": tag.find(class_="trackTitle").text,
            "artist": tag.find(class_="artistTitle").text,
            "album": "no album on bugs",
            "rank": rank,
        }
        rank += 1
    return ranking

print(prettifyDictionary(getRanking()))