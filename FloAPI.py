import time
import requests as r
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from MelonAPI import prettifyDictionary

url = "https://www.music-flo.com/browse"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

def getRanking():
    ranking = {}
    rank = 1
    time.sleep(10)
    button = driver.find_element(By.CLASS_NAME, "btn_list_more")
    button.send_keys(Keys.RETURN)
    allTags = driver.find_elements(By.TAG_NAME, "tr")
    for tag in allTags:{
        "title": tag.find_element(By.CLASS_NAME, "tit__text").text,
        "artist": tag.find_element(By.CLASS_NAME, "last").text,
        "album": tag.find_element(By.CLASS_NAME, "album").text,
        "rank": rank,
    }
    return ranking

result = getRanking()
driver.quit

print(prettifyDictionary(result))
# print(prettifyDictionary(result[15]['title']))