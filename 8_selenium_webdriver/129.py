#
# * 129. Retrieving the text between HTML tags

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

text_of_element = driver.find_element(By.ID, "pah").text

print(text_of_element)

button_label = driver.find_element(By.ID, "button9").text

print(button_label)


driver.quit()