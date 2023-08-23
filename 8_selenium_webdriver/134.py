#
# * 134. Retrieving the value of any HTML elements attribute

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")


c = driver.find_element(By.ID, "ta1").get_attribute("cols")

print(c)

button_label = driver.find_element(By.XPATH, "(//input[@title='search'])[2]").get_attribute("value")

print(button_label)

driver.quit()