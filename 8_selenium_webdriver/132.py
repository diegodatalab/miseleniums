#
# * 132. Closing the *current* browser window

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

time.sleep(3)

driver.find_element(By.LINK_TEXT, 'Open a popup window').click()

time.sleep(3)

driver.close()

