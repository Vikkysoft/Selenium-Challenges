#  Using any browser navigate to any Youtube video of your choice,
#  allow your script to wait for the comments to load then get the first two comments,
#  and print them in the terminal.

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


def comment_is_visible(driver):
    web_driver_wait = WebDriverWait(driver, 50)
    web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="count"]/yt-formatted-string/span[2]')))
    comments = driver.find_elements(By.XPATH, '//*[@id="content-text"]')
    for comment in comments:
        comment_text = comment.find_element(By.ID, 'content-text')
        print(comment_text.text)

    time.sleep(10)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.youtube.com/watch?v=FOLeWdj9gXg")


if __name__ == '__main__':
    main()
