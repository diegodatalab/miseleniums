#
# * 232. JavaScript Executor

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

driver.execute_script("alert('diego teste')")

# time.sleep(3)

# driver.execute_script("prompt('enter your name: ')")

# driver.execute_script("confirm('are you sure? ')")

time.sleep(3)

driver.quit()
