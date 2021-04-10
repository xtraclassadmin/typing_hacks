import os
from selenium import webdriver
import time


def init_driver():
    chromedriver = "/Users/abhijeetsinghkhangarot/Downloads/chromedriver"
    driver = webdriver.Chrome(chromedriver)
    return driver


def type(driver):
    driver.get("https://10fastfingers.com/typing-test/english")
    time.sleep(5)
    input_box = driver.find_element_by_id('inputfield')
    i = 0
    while True:
        word = driver.find_element_by_xpath("//span[@wordnr='" + str(i) + "']")
        input_box.send_keys(word.text)
        input_box.send_keys(" ")
        i += 1


if __name__ == "__main__":
    driver = init_driver()
    type(driver)
