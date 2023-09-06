import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager

service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
# driver = webdriver.Chrome()
start = time.time()
driver = webdriver.Chrome(service=service, options=options)



driver.get('http://www.google.com')
