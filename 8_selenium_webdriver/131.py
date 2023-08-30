#
# * 131. Retrieving the URL of the current web page

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

url_one = driver.current_url

print(url_one)

driver.find_element(By.LINK_TEXT, "compendiumdev").click()

url_two = driver.current_url

print(url_two)

driver.quit()