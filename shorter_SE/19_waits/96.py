#
# * 96. PageLoad Timeout in Selenium Python

# ? Timeout interface manage all the waits in Selenium

"""Timeout abstract methods:
implicitlywait()
setScriptTimeout()
pageLoadTimeout()
"""

# * pageloadtimeout() => set the limit for a page to load
# ! if page not loaded within the given time limit then selenium will throw the TimeoutException

import time
from selenium import webdriver

url = "https://edition.cnn.com/"


def test_selenium_waits():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.set_page_load_timeout(120) # test to identify loading time
    driver.get(url)
