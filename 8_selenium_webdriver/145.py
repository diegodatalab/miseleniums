#
# * 145. Taking screen-shot of the web page

# ! tip: do not use 'relative path'

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://tutorialsninja.com/demo/index.php?route=account/login")
driver.save_screenshot("/home/diego/Desktop/stout_selenium/8_selenium_webdriver/screenshots/145.png")        

# ! the same as .get_screenshot_as_file()
# driver.get_screenshot_as_file("/home/diego/Desktop/stout_selenium/8_selenium_webdriver/screenshots/145.png")
driver.quit()