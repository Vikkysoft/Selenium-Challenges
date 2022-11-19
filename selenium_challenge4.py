# Navigate to https://www.bbc.com/  and  print  out  the
# top 10 latest news from the home page.

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.bbc.com/")
    driver.maximize_window()
    news_headlines = driver.find_element(By.XPATH,
                                         '//*[@id="page"]/section[4]/div/div/div[2]/div/section[1]/div/ul/li[1]/div/div[2]/h3/a')
    news_headline = driver.find_elements(By.CLASS_NAME, 'media__link')
    # for news in news_headline:
    # print("News:", news.text)
    number = 0
    while number < 10:
        print(news_headline[number].text)
        number += 1


if __name__ == '__main__':
    main()
