from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

def test_keep_browser_open():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.get('http://selenium.dev')

    driver.quit()