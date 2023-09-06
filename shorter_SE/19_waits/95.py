#
# * 95. Waits in Selenium

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://omayo.blogspot.com/"


def test_selenium_waits():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)

    btn = driver.find_element(By.XPATH, "//button[@class='dropbtn']")
    btn.click()
    time.sleep(5)

    driver.find_element(By.XPATH, "//a[normalize-space()='Gmail']")

    driver.quit()

# //*[@id="gsr"]
