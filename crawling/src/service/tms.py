from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from src.repository.tms_repository import findBoard

def run():
    webtoonTitle = input("웹툰 제목을 입력하세요 > ")

    foundWebtoon = findBoard(webtoonTitle)

    if not foundWebtoon:
        return

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://koritbs.cafe24.com/student/index.php")
    driver.maximize_window()
    sleep(1)

    loginId = driver.find_element(by=By.CSS_SELECTOR, value="body > div > form > table > tbody > tr:nth-child(3) > td > input")
    loginId.send_keys("ehdgus0837")
    loginPw = driver.find_element(by=By.CSS_SELECTOR, value="body > div > form > table > tbody > tr.border-left-danger.border-right-danger.border-bottom-0.border-top-0.bg-brown > td > input")
    loginPw.send_keys("hongdong2@")
    loginButton = driver.find_element(by=By.CSS_SELECTOR, value="body > div > form > table > tbody > tr.border-left-danger.border-right-danger.border-bottom-danger.border-top-0.bg-brown > td > div > div:nth-child(2) > button")
    loginButton.click()
    sleep(2)

    iotButton = driver.find_element(by=By.CSS_SELECTOR, value="body > table > tbody > tr:nth-child(2) > td:nth-child(2) > table > tbody > tr.hover.pointer")
    iotButton.click()
    sleep(2)

    crawlingButton = driver.find_element(by=By.CSS_SELECTOR, value="body > table > tbody > tr:nth-child(2) > td:nth-child(2) > ul > li:nth-child(10) > div")
    crawlingButton.click()
    sleep(2)

    uploadButton = driver.find_element(by=By.CSS_SELECTOR, value="body > table > tbody > tr:nth-child(2) > td:nth-child(2) > form > table > caption > div > div:nth-child(2) > div > a")
    uploadButton.click()
    sleep(2)

    title = driver.find_element(by=By.CSS_SELECTOR, value="body > table > tbody > tr:nth-child(2) > td:nth-child(2) > form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input")
    title.send_keys(f"홍동현 (웹툰 제목:{foundWebtoon["title"]})")

    body = driver.find_element(by=By.CSS_SELECTOR, value="body > table > tbody > tr:nth-child(2) > td:nth-child(2) > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > div.ck.ck-editor__main > div")
    body.send_keys(f"""
title: {foundWebtoon["webtoon_id"]}
author: {foundWebtoon["author"]}
rating: {foundWebtoon["rating"]}
imgUrl: {foundWebtoon["img_url"]}
categoryName: {foundWebtoon["category_name"]}""")

    sendButton = driver.find_element(by=By.CSS_SELECTOR, value="body > table > tbody > tr:nth-child(2) > td:nth-child(2) > form > table > tbody > tr.end > td > button")
    sendButton.click()
    sleep(2)