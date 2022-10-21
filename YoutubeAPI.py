from re import I
import time
from TestCases import prettifyDictionary
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


url = "https://charts.youtube.com/charts/TopSongs/kr"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

def getRanking():
    ranking = {}
    rank = 1
    time.sleep(1)
    title = driver.find_elements(By.XPATH, './/span[@class="ytmc-ellipsis-text style-scope"]')
    artist = driver.find_elements(By.XPATH, './/div[@class="ytmc-artists-list-container style-scope ytmc-artists-list"]')
    for i in range(len(artist)):
        ranking[rank] = {
            # youtube has a top banner with two extra 'ytmc-ellipsis-text style-scope' span classes for the No. 1 song so we skip them to get the top 100
            "title": title[i+2].text,
            "artist": artist[i].text,
            "album": "no album on youtube",
            "rank": rank
        }
        rank += 1
    driver.quit
    return ranking


print(prettifyDictionary(getRanking()))
