import time
from selenium import webdriver

# * 198. Selenium 4 - Handling Multiple Window commands


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

app_one_title = driver.title
print(app_one_title)

time.sleep(3)

driver.switch_to.new_window('window')

driver.get('http://selenium143.blogspot.com/')

time.sleep(3)

app_two_title = driver.title
print(app_two_title)

time.sleep(3)

driver.quit()