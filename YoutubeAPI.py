from re import I
import time
from TestCases import prettifyDictionary
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://charts.youtube.com/charts/TopSongs/kr"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

def getRanking():
    ranking = {}
    rank = 1
    delay = 3
    # delay is necessary, because the youtube app needs to load
    try:
        element_present = EC.presence_of_element_located((By.XPATH, './/span[@class="ytmc-ellipsis-text style-scope"]'))
        WebDriverWait(driver, delay).until(element_present)
    except TimeoutException:
        print ("Page could not be loaded")
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
