#
# * 161. Default Page Load Timeout for Web Pages

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://selenium143.blogspot.com"

driver = webdriver.Firefox()
driver.maximize_window()
driver.get(url)

driver.find_element(By.LINK_TEXT, "What is Selenium?").click()