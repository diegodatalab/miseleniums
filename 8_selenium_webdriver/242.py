#
# * 242. Refreshing a Page using JavaScript in Selenium
# ! faster than selenium command 'driver.refresh()'
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://selenium143.blogspot.com/")

driver.execute_script('history.go(0)')

time.sleep(3)

driver.quit()