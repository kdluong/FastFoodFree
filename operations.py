from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def open_browser(WEBSITE):
    # options = Options()
    # options.binary_location = '/opt/headless-chromium'
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--single-process')    # optional
    # options.add_argument('--disable-dev-shm-usage')

    # driver = webdriver.Chrome('/opt/chromedriver',options=options)

    driver = webdriver.Chrome()
    driver.get(WEBSITE)

    return driver


def click_button(driver, button_id):
    driver.find_element(By.ID, button_id).click()


def find_text(driver, name):
    return driver.find_elements(By.NAME, name)


def type_value(driver, id, value):
    driver.find_element(By.ID, id).send_keys(value)
