import time
from selenium import webdriver

# * 191. Executing JavaScript code using Selenium Python



driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

time.sleep(3)

driver.execute_script("alert('Diego?')")

time.sleep(3)

driver.quit()