#
# * 150. Setting page load time out for the website to open

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

# ? .set_page_load_timeout(time in seconds) -> if the time exceeds, report an exception
driver.set_page_load_timeout(3)

driver.get("https://selenium143.blogspot.com/")

driver.quit()

