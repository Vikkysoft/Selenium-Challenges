import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def send_keys_to_element(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.google.com")
    driver.maximize_window()
    action = ActionChains(driver)
    send_keys_to_element(driver.find_element(By.NAME, "q"), "Python", Keys.ENTER)
    time.sleep(2)
    wikipedia_brief_text = driver.find_element(By.TAG_NAME, "h3")
    print("Wikipedia brief:", wikipedia_brief_text.text)
    time.sleep(5)
    driver.close()


if __name__ == "__main__":
    main()
