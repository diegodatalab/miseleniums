#
# * 222. Retrieving Table data in first row

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://omayo.blogspot.com/"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

tb_first_row = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr[1]/td")

for data in tb_first_row:
    print(data.text)

driver.quit()
