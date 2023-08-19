
# * 127. Storing the Element to perform multiple operations on same element

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(2)
text_field_one = driver.find_element(By.ID, "textbox1")
text_field_one.clear()
time.sleep(2)
text_field_one.send_keys("Diego")
time.sleep(2)
text_field_one.clear()
time.sleep(2)
text_field_one.send_keys("Selenium")
time.sleep(2)
text_field_one.clear()
