from bs4 import BeautifulSoup
import requests as r
import json as js

from MelonAPI import prettifyDictionary

url1 = "https://genie.co.kr/chart/top200?ditc=D&ymd=20220906&hh=19&rtm=Y&pg=1"
url2 = "https://genie.co.kr/chart/top200?ditc=D&ymd=20220906&hh=19&rtm=Y&pg=2"

html1 = r.get(url1, headers={"User-Agent": "XY"})
html2 = r.get(url2, headers={"User-Agent": "XY"})

def getRanking():
    doc = BeautifulSoup(html1.text, "html.parser")
    allTags = doc("tr", attrs={"songid": True})
    ranking = {}
    rank = 1
    for tag in allTags:
        ranking[rank] = {
            "title": tag.find(class_="title ellipsis").text.strip(),
            "artist": tag.find(class_="artist ellipsis").text.replace('\n', ''),
            "album": tag.find(class_="albumtitle ellipsis").text.replace('\n', ''),
            "rank": rank,
        }
        rank += 1
    doc2 = BeautifulSoup(html2.text, "html.parser")
    allTags2 = doc2("tr", attrs={"songid": True})
    for tag in allTags2:
        ranking[rank] = {
            "title": tag.find(class_="title ellipsis").text.strip(),
            "artist": tag.find(class_="artist ellipsis").text.replace('\n', ''),
            "album": tag.find(class_="albumtitle ellipsis").text.replace('\n', ''),
            "rank": rank,
        }
        rank += 1
    return ranking

result = getRanking()
print(prettifyDictionary(result))