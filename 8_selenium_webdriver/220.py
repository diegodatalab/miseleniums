# 
# * 220. Retrieving Table headings

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

table_headings = driver.find_elements(By.XPATH, "//table[@id='table1']//th")

for heading in table_headings:
    print(heading.text)

driver.quit()