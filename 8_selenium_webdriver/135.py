#
# * 135. Checking whether the element is displayed on the page


from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

if driver.find_element(By.ID, "ta1").is_displayed():
    print("displayed")
else:
    print('not displayed')

driver.quit()