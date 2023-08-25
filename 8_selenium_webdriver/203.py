#
# * 203. Wait for the Presence of Element
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

driver.find_element(By.CLASS_NAME, 'dropbtn').click()
time.sleep(3)

wait = WebDriverWait(driver, 20)
flipkart_option = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Flipkart')))
time.sleep(2)

flipkart_option.click()

time.sleep(2)
driver.quit()