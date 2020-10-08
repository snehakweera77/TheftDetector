# https://en.savefrom.net/1-youtube-video-downloader-4/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

def downloadVid(PATH, link) :
    driver = webdriver.Chrome(PATH)
    driver.get("https://en.savefrom.net/1-youtube-video-downloader-4/")
    search = driver.find_element_by_name("sf_url")
    search.send_keys(link)
    search.send_keys(Keys.RETURN)

    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable ((By.XPATH, '/html/body/div/div[1]/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/a'))
        ).click()

    finally:
        time.sleep(10)
    time.sleep(10)
    driver.quit()

def main():
    PATH = "F:\sneha\chromedriver.exe"

    with open('videoLinks.txt', 'r') as file:
        for row in file.readlines():
            downloadVid(PATH, row)
            time.sleep(3)

if __name__ == "__main__":
    main()