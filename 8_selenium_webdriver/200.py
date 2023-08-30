#
# * 200. Waiting Mechanism - Implicit and Explicit

import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

url = "https://omayo.blogspot.com/"

driver = webdriver.Chrome()
driver.maximize_window()

# ! antes do driver.get(url)
# ! 'implicity wait' -> uma vez criado no começo do script, se aplica a todos os elementos do script/pagina
# ! desvantagem: 
"""
se algum 'locator' estiver errado, o implicity wait vai continuar procurando, ao inves de
lançar logo uma exceção
"""
# ! é um 'global wait'
# ! não colocar mais que 10 segundos 
driver.implicitly_wait(10)

driver.get(url)

driver.find_element(By.CLASS_NAME, 'dropbtn').click()

wait = WebDriverWait(driver, 30)

flipkart_option = wait.until(EC.visibility_of_element_located((By. LINK_TEXT, 'Flipkart')))

flipkart_option.click()

# driver.find_element(By. LINK_TEXT, 'Flipkart').click()

time.sleep(3)
driver.quit()