#
# * 245. Scrapping the text from the Page

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

text_on_page = str(driver.execute_script("return document.documentElement.innerText"))

print(text_on_page)

driver.quit()