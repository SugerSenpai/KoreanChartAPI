import time
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
    button = driver.find_element(By.CLASS_NAME, "btn_list_more")
    button.send_keys(Keys.RETURN)
    title = driver.find_elements(By.CLASS_NAME, "tit__text")
    artist = driver.find_elements(By.CLASS_NAME, "last")
    album = driver.find_elements(By.CLASS_NAME, "album")
    for i in range(len(title)):
        ranking[rank] = {
            "title": title[i].text.strip(),
            "artist": artist[i].text.strip(),
            "album": album[i].text.strip(),
            "rank": rank
        }
        rank +=1
    driver.quit
    return ranking

result = getRanking()

print(prettifyDictionary(result))
# print(prettifyDictionary(result[15]['title']))