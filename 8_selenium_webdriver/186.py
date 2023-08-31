#
# * 186. pause() ActionChains command

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url = "https://tutorialsninja.com/demo/index.php?route=account/register"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

driver.find_element(By.ID, 'input-firstname').send_keys('ogeid')

actions = ActionChains(driver)
actions.send_keys(Keys.TAB).pause(3)\
    .send_keys('avlis').send_keys(Keys.TAB).pause(3)\
    .send_keys('sdiegobarbosa@gmail.com')\
    .send_keys(Keys.TAB).pause(3)\
    .send_keys('123456')\
    .send_keys(Keys.TAB).pause(3)\
    .send_keys('651651')\
    .send_keys(Keys.TAB).pause(3)\
    .send_keys('651651')\
    .send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).pause(3)\
    .send_keys(Keys.SPACE).send_keys(Keys.TAB).pause(3)\
    .send_keys(Keys.ENTER).pause(5).perform()

driver.quit()