#
# * 221. Retrieving Table data

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

table_data = driver.find_elements(By.XPATH, "//table[@id='table1']//td")

for data in table_data:
    print(data.text)


driver.quit()