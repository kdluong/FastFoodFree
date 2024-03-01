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

def find_error(driver, error_name):
    return driver.find_elements(By.NAME, error_name)

def clickButtonRange(driver, startRange, endRange, stopAt, optionNumber):

    count = 0

    for i in range(startRange, endRange + 1):
        if(i < 10): test = "R00000"
        elif(i < 100): test = "R0000"
        else: test = "R000"
        try:  
            click_button(driver, test + str(i) + '.' + optionNumber)
            count += 1
            if(count == stopAt): 
                break
        except:
            pass

def clickDropList(driver, listID, listOption):
    Select(driver.find_element_by_id(listID)).select_by_visible_text(listOption)

def type_value(driver, id, value):
    driver.find_element(By.ID, id).send_keys(value)

def getText(driver, xPath):
    return driver.find_element_by_xpath(xPath).text