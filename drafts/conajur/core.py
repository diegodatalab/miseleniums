import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url = "https://internet-consultapublica.apps.sefaz.ce.gov.br/contencioso/preparar-consultar"

options = Options()
# options.add_argument("--headless")
# options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(url)

ano_entrada = driver.find_element(By.XPATH, "//input[@id='numano']")

ano_entrada.send_keys('2023')
time.sleep(10)
driver.close()