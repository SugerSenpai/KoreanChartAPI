from Util import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.music-flo.com/browse"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)


def getRanking():
    ranking = {}
    rank = 1
    delay = 3
    # because flo app needs to load we add a delay
    try:
        element_present = EC.presence_of_element_located(
            (By.CLASS_NAME, "btn_list_more"))
        WebDriverWait(driver, delay).until(element_present)
    except TimeoutException:
        print("Page could not be loaded")
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
        rank += 1
    driver.quit()
    return prettifyDictionary(ranking)


print(getRanking())