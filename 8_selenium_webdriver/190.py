#
# * 190. Taking Screenshot of a Page Section

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

section_one = driver.find_element(By.ID, "LinkList1")

section_one.screenshot("/home/diego/Desktop/stout_selenium/8_selenium_webdriver/screenshots/190.png")

driver.quit()



