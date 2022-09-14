import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from MelonAPI import prettifyDictionary

url = "https://charts.youtube.com/charts/TopSongs/kr"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

def getRanking():
    ranking = {}
    rank = 1
    # delay is necessary, because the youtube app need to load
    time.sleep(1)
    title = driver.find_elements(By.XPATH, '//span[@class="ytmc-ellipsis-text style-scope"]')
    artist = driver.find_elements(By.XPATH, '//span[@class="ytmc-artist-name clickable style-scope ytmc-artists-list"]')
    for i in range(len(artist)):
        ranking[rank] = {
            # because youtube has 2 extra classes for their top banner, we need to start the array with +2
            "title": title[i+2].text,
            "artist": artist[i].text,
            "album": "no album on youtube",
            "rank": rank
        }
        rank += 1
    driver.quit
    return ranking

result = getRanking()

print(prettifyDictionary(result))
# print(prettifyDictionary(result[15]['title']))