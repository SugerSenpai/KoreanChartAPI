from bs4 import BeautifulSoup
from TestCases import prettifyDictionary
import requests as r

url = "https://vibe.naver.com/chart/domestic"

html = r.get(url, headers={"User-Agent": "XY"})


def getRanking():
    doc = BeautifulSoup(html.text, "html.parser")
    allTags = doc("tr", class_={"song": True})
    ranking = {}
    rank = 1
    print(allTags)
    for tag in allTags:
        ranking[rank] = {
            "title": tag.find(class_="link_text").text.replace('\n', ''),
            "artist": tag.find(class_="artist_sub").text.replace('\n', ''),
            "album": "no album on naver",
            "rank": rank,
        }
        rank += 1
    return ranking

print(prettifyDictionary(getRanking()))