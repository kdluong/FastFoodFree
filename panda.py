from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
from operations import *


def input_survey_code(driver, survey_code):
    for index in range(0, 6):
        type_value(driver, "CN" + str(index + 1), survey_code[index])

    click_button(driver, "NextButton")

    # remove 2 in production

    click_button(driver, "NextButton")
    click_button(driver, "NextButton")

    return not find_error(driver, "ErrorMessageOnTopOfThePage")


def panda_express(email, rating, survey_code):

    WEBSITE = "https://www.pandaguestexperience.com/Index.aspx?ADACompliance=true"

    try:

        # Launch browser and navigate to the website

        driver = open_browser(WEBSITE)

        # Enter survey code

        if not input_survey_code(driver, survey_code):
            raise Exception("Invalid Survey Code: Please check and try again.")

        print("Valid Survey Code")

        # Please rate your overall satisfaction with your Panda Express experience

        # input("Press Enter to close the browser...")

        # 1: Please rate your overall satisfaction with your Panda Express experience.

        # clickButton(driver, "R000002" + "." + rating)
        # clickButton(driver, "NextButton")

        # 1A:

        # if(int(rating) == 1):
        #     clickButton(driver, "R000003.1")
        #     clickButton(driver, "NextButton")

        # 2

        # clickButton(driver, "R000005.5")
        # clickButton(driver, "NextButton")

        # 3

        # clickButton(driver, "R000006.2")
        # clickButton(driver, "NextButton")

        # 4

        # clickButtonRange(driver, 0, 299, 6, rating)
        # clickButton(driver, "NextButton")

        # 5

        # clickButtonRange(driver, 0, 299, 6, rating)
        # clickButton(driver, "NextButton")

        # 6

        # clickButton(driver, "NextButton")

        # 6A:

        # if(int(rating) < 4):
        #     clickButton(driver, "NextButton")
        #     clickButton(driver, "NextButton")
        #     clickButton(driver, "NextButton")
        #     clickButton(driver, "NextButton")

        # 7

        # clickButton(driver, "R000069.2")
        # clickButton(driver, "NextButton")

        # 8

        # clickButton(driver, "R000073" + "." + rating)
        # clickButton(driver, "R000141" + "." + rating)
        # clickButton(driver, "R000074" + "." + rating)
        # clickButton(driver, "NextButton")

        # 9

        # clickButton(driver, "NextButton")

        # 10

        # clickButton(driver, "R000078" + "." + rating)
        # clickButton(driver, "NextButton")

        # 10A:

        # if(int(rating) < 4):
        #     clickButton(driver, "NextButton")

        # 11

        # clickButton(driver, "R000381" + "." + rating)
        # clickButton(driver, "NextButton")

        # 11A:

        # if(int(rating) < 3):
        #     clickButton(driver, "R000080.2")
        # else:
        #     clickButton(driver, "R000080.1")
        # clickButton(driver, "NextButton")

        # 12

        # clickButton(driver, "R000087.1")
        # clickButton(driver, "NextButton")

        # 13

        # clickButton(driver, "R000089.2")
        # clickButton(driver, "NextButton")

        # 14

        # clickButton(driver, "R000092." + str(abs(5 - (int(rating) - 1))))    # apple pie
        # clickButton(driver, "NextButton")

        # 15

        # clickButton(driver, "NextButton")

        # 16

        # clickButtonRange(driver, 118, 121, 4, rating)
        # clickButton(driver, "NextButton")

        # 17

        # if(abs(5 - (int(rating) - 1)) > 3):
        #     clickButtonRange(driver, 123, 128, 5, '3') # 1, 2, 3
        # elif(abs(5 - (int(rating) - 1)) == 3):
        #     clickButtonRange(driver, 123, 128, 5, '2') # 1, 2, 3
        # else:
        #     clickButtonRange(driver, 123, 128, 5, '1') # 1, 2, 3
        # clickButton(driver, "NextButton")

        # 18

        # clickButton(driver, "NextButton")

        # 19

        # clickDropList(driver, 'R000130', 'Prefer not to answer')
        # clickDropList(driver, 'R000131', 'Prefer not to answer')
        # clickDropList(driver, 'R000132', 'Prefer not to answer')
        # clickDropList(driver, 'R000133', 'Prefer not to answer')
        # clickButton(driver, "NextButton")

        # 20

        # type(driver, "S000057", email)
        # type(driver, "S000064", email)
        # clickButton(driver, "NextButton")

        # 21

        # answer = getText(driver, '//*[@id="finishIncentiveHolder"]/p[2]')

        # driver.close()
        # driver.quit()

        # return {
        #     'statusCode': 200,
        #     'headers': {
        #         'Content-Type': 'application/json',
        #         'custom-header': 'some-value'
        #     },
        #     'body': json.dumps(answer),
        #     'cookies': [
        #         "samplecookie=samplevalue",
        #     ],
        #     'isBase64Encoded': False
        # }

        # Terminate browser

        driver.quit()

        return "Success"

    except Exception as e:
        return e
