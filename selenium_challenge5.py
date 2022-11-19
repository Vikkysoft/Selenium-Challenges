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


def scroll_by_offset(action, delta_y):
    action.scroll_by_amount(0, delta_y).perform()


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.youtube.com/watch?v=FOLeWdj9gXg")
    action = ActionChains(driver)
    driver.maximize_window()

    scroll_by_offset(action, 500)
    web_driver_wait = WebDriverWait(driver, 50)
    web_driver_wait.until(EC.visibility_of_element_located(By.TAG_NAME), "ytd-item-section-renderer")
    comments = driver.find_element(By.TAG_NAME, "ytd-item-section-renderer")
    for comment in comments:
        comment_content = comment.find_element(By.ID, 'content-text')
        print(comment_content.text)

    time.sleep(10)


if __name__ == '__main__':
    main()
