# from bs4 import BeautifulSoup
# import requests as r

# from MelonAPI import prettifyDictionary

# url = "https://charts.youtube.com/charts/TopSongs/kr"
# html = r.get(url, headers={"User-Agent": "XY"})

# def getRanking():
#     doc = BeautifulSoup(html.text, "html.parser")
#     allTags = doc("div", attrs={"track-video-id": True})
#     print(doc)
#     ranking = {}
#     rank = 1
#     for tag in allTags:
#         ranking[rank] = {
#             "title": tag.find(class_="ytmc-ellipsis-text style-scope").text.replace('\n', ''),
#             "artist": tag.find(class_="ytmc-artist-name clickable style-scope ytmc-artists-list").text.replace('\n', ''),
#             "album": "no album on youtube",
#             "rank": rank,
#         }
#         rank += 1
#     return ranking

# result = getRanking()

# print(prettifyDictionary(result))
# print(prettifyDictionary(result[15]['title']))