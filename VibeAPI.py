from Util import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://vibe.naver.com/chart/domestic"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
# window need to be maximized for us to find all elements
driver.maximize_window()


def getRanking():
    ranking = {}
    rank = 1
    delay = 3
    # delay is necessary, because the vibe app needs to load
    try:
        element_present = EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div[2]/div/div/a[2]'))
        WebDriverWait(driver, delay).until(element_present)
    except TimeoutException:
        print("Page could not be loaded")
    driver.find_element(
        By.XPATH, '//*[@id="app"]/div[2]/div/div/a[2]').send_keys(Keys.RETURN)
    title = driver.find_elements(By.XPATH, './/div[@class="title_badge_wrap"]')
    artist = driver.find_elements(By.XPATH, './/td[@class="artist"]/span')
    album = driver.find_elements(By.XPATH, './/a[@class="link"]')
    for i in range(len(title)):
        ranking[rank] = {
            "title": title[i].text,
            "artist": artist[i].text.replace("\n", ", "),
            "album": album[i].text,
            "rank": rank
        }
        rank += 1
    driver.quit
    return ranking


print(prettifyDictionary(getRanking()))
