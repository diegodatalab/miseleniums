#
# * 141. Retrieving the HTML Source Code of the Web Page

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://testpages.herokuapp.com/basic_web_page.html")

html_source_code = driver.page_source
print(html_source_code)

driver.quit()