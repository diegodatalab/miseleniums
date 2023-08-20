#
# * 189. Taking Screenshot of a Web Element

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")

search_button = driver.find_element(By.XPATH, "//div[@id='search']//button")

search_button.screenshot('/home/diego/Desktop/stout_selenium/8_selenium_webdriver/screenshots/189.png')

driver.quit()