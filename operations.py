from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

def clickButton(driver, buttonID):
    driver.find_element_by_id(buttonID).click()

def clickButtonRange(driver, startRange, endRange, stopAt, optionNumber):

    count = 0

    for i in range(startRange, endRange + 1):
        if(i < 10): test = "R00000"
        elif(i < 100): test = "R0000"
        else: test = "R000"
        try:  
            clickButton(driver, test + str(i) + '.' + optionNumber)
            count += 1
            if(count == stopAt): 
                break
        except:
            pass

def clickDropList(driver, listID, listOption):
    Select(driver.find_element_by_id(listID)).select_by_visible_text(listOption)

def type(driver, textFieldName, text):
    driver.find_element_by_name(textFieldName).send_keys(text)

def getText(driver, xPath):
    return driver.find_element_by_xpath(xPath).text