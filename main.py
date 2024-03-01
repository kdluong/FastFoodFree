from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import json

#panda, mcd, jack
# 4 & 5 work, 1 2 3 doesn't

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

def main(event, context):
    website = "https://www.pandaguestexperience.com/Index.aspx?ADACompliance=true"
    email = "kluong264@gmail.com"
    rating = "1"

    options = Options()
    options.binary_location = '/opt/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome('/opt/chromedriver',chrome_options=options)

    #driver = webdriver.Chrome(options=options)
    driver.get(website)

    type(driver, "CN1", 1234)
    type(driver, "CN2", 1234)
    type(driver, "CN3", 1234)
    type(driver, "CN4", 1234)
    type(driver, "CN5", 1234)
    type(driver, "CN6", 12)

    clickButton(driver, "NextButton")
    clickButton(driver, "NextButton")
    clickButton(driver, "NextButton")

    clickButton(driver, "R000002" + "." + rating)
    clickButton(driver, "NextButton")

    if(int(rating) == 1):
        clickButton(driver, "R000003.1")
        clickButton(driver, "NextButton")

    clickButton(driver, "R000005.5")
    clickButton(driver, "NextButton")

    clickButton(driver, "R000006.2")
    clickButton(driver, "NextButton")

    clickButtonRange(driver, 0, 299, 6, rating)
    clickButton(driver, "NextButton")

    clickButtonRange(driver, 0, 299, 6, rating)
    clickButton(driver, "NextButton")

    clickButton(driver, "NextButton")

    if(int(rating) < 4):
        clickButton(driver, "NextButton")
        clickButton(driver, "NextButton")
        clickButton(driver, "NextButton")
        clickButton(driver, "NextButton")

    clickButton(driver, "R000069.2") 
    clickButton(driver, "NextButton")

    clickButton(driver, "R000073" + "." + rating) 
    clickButton(driver, "R000141" + "." + rating) 
    clickButton(driver, "R000074" + "." + rating) 
    clickButton(driver, "NextButton")

    clickButton(driver, "NextButton")

    clickButton(driver, "R000078" + "." + rating) 
    clickButton(driver, "NextButton")

    if(int(rating) < 4):
        clickButton(driver, "NextButton")

    clickButton(driver, "R000381" + "." + rating) 
    clickButton(driver, "NextButton")

    if(int(rating) < 3):
        clickButton(driver, "R000080.2")    
    else:
        clickButton(driver, "R000080.1")
    clickButton(driver, "NextButton")

    clickButton(driver, "R000087.1") 
    clickButton(driver, "NextButton")

    clickButton(driver, "R000089.2") 
    clickButton(driver, "NextButton")

    clickButton(driver, "R000092." + str(abs(5 - (int(rating) - 1))))    # apple pie
    clickButton(driver, "NextButton")

    clickButton(driver, "NextButton")

    clickButtonRange(driver, 118, 121, 4, rating)
    clickButton(driver, "NextButton")

    if(abs(5 - (int(rating) - 1)) > 3):
        clickButtonRange(driver, 123, 128, 5, '3') # 1, 2, 3
    elif(abs(5 - (int(rating) - 1)) == 3):
        clickButtonRange(driver, 123, 128, 5, '2') # 1, 2, 3
    else:
        clickButtonRange(driver, 123, 128, 5, '1') # 1, 2, 3
    clickButton(driver, "NextButton")

    clickButton(driver, "NextButton")

    clickDropList(driver, 'R000130', 'Prefer not to answer')
    clickDropList(driver, 'R000131', 'Prefer not to answer')
    clickDropList(driver, 'R000132', 'Prefer not to answer')
    clickDropList(driver, 'R000133', 'Prefer not to answer')
    clickButton(driver, "NextButton")

    type(driver, "S000057", email)
    type(driver, "S000064", email)
    clickButton(driver, "NextButton")

    answer = getText(driver, '//*[@id="finishIncentiveHolder"]/p[2]')

    driver.close()
    driver.quit()

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'custom-header': 'some-value'
        },
        'body': json.dumps(answer),
        'cookies': [
            "samplecookie=samplevalue",
        ],
        'isBase64Encoded': False
    }