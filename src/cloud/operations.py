from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver

def open_browser(WEBSITE):

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    driver.get(WEBSITE)

    return driver

def click_button(driver, button_id):
    driver.find_element(By.ID, button_id).click()

def find_text_name(driver, name):
    return driver.find_elements(By.NAME, name)

def find_text_id(driver, id):
    return driver.find_elements(By.ID, id)

def type_value(driver, id, value):
    driver.find_element(By.ID, id).send_keys(str(value))