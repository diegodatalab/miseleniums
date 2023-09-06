# chromedriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def verify_title():
    # navigate to the website
    driver.get("https://sdetunicorns.com")

    # get the title of the page
    title = driver.title

    # verify the title
    expected_title = "uhhh lala la"
    if title == expected_title:
        print('ok')
    else:
        print('failed')

    # close the browser
    driver.quit()


if __name__ == '__main__':
    verify_title()