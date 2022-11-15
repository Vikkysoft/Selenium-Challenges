import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def send_keys_to_element(element, keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://weather.com/")
    driver.maximize_window()
    # send_keys_to_element(driver.find_element(By.CSS_SELECTOR, "#LocationSearch_input"), "Ibadan")
    time.sleep(2)
    current_temperature = driver.find_element(By.XPATH, '//*[@id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034"]/div/section/div/div[2]/div[1]/div[1]/span')
    print("Current temperature is:", current_temperature.text)
    morning_temperature = driver.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a"]/section/div/ul/li[1]/a/div[1]/span')
    print("Morning temperature is:", morning_temperature.text)
    afternoon_temperature = driver.find_element(By.CSS_SELECTOR, '#WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a > section > div > ul > li.Column--column--3tAuz.Column--active--27U5T > a > div.Column--temp--1sO_J > span')
    print("Afternoon temperature is:", afternoon_temperature.text)
    evening_temperature = driver.find_element(By.CSS_SELECTOR, '#WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a > section > div > ul > li:nth-child(3) > a > div.Column--temp--1sO_J > span')
    print("Evening temperature is:", evening_temperature.text)
    overnight_temperature = driver.find_element(By.CSS_SELECTOR, '#WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a > section > div > ul > li:nth-child(4) > a > div.Column--temp--1sO_J > span')
    print("Overnight temperature is:", overnight_temperature.text)



if __name__ == "__main__":
    main()
