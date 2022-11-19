# Using    the    chrome    browser    navigate    to https://www.facebook.com/
# Fill  in  the  email/phone  and password text box then click the Login Button.

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def send_keys_to_element(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com/ ")
    driver.maximize_window()
    time.sleep(2)
    send_keys_to_element(driver.find_element(By.NAME, "email"), "graceb91@gmail.com")
    time.sleep(2)
    send_keys_to_element(driver.find_element(By.NAME, "pass"), "daradami1418")
    time.sleep(2)
    driver.find_element(By.NAME, "login").click()
    time.sleep(10)


if __name__ == "__main__":
    main()
