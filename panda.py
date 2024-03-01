from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
from operations import *


def input_survey_code(driver, survey_code):
    for index in range(0, 6):
        type_value(driver, "CN" + str(index + 1), survey_code[index])

    click_next(driver)

    # remove 2 in production

    click_next(driver)
    click_next(driver)

    return not find_text(driver, "ErrorMessageOnTopOfThePage")


def click_next(driver):
    click_button(driver, "NextButton")


def give_review(driver, rating, options):

    for option in options:
        if driver.find_elements(By.ID, option[0]):
            click_button(driver, option[1] + rating)

    click_next(driver)


def pause():
    input("Press Enter to close the browser...")


def panda_express(email, rating, visit_type, survey_code):

    WEBSITE = "https://www.pandaguestexperience.com/Index.aspx?ADACompliance=true"

    food_options = [
        ("textR000012", "R000012."),
        ("textR000015", "R000015."),
        ("textR000010", "R000010."),
        ("textR000011", "R000011."),
        ("textR000018", "R000018."),
        ("textR000020", "R000020."),
        ("textR000013", "R000013."),
        ("textR000016", "R000016."),
        ("textR000008", "R000008."),
        ("textR000021", "R000021."),
        ("textR000015", "R000015."),
    ]

    recommendation_options = [
        ("textR000074", "R000074."),
        ("textR000073", "R000073."),
        ("textR000141", "R000141."),
        ("textR000072", "R000072."),
    ]

    bad_review_options = [
        "R000504",
        "R000299",
        "R000045",
        "R000052",
        "R000061",
        "R000030",
        "R000038",
        "R000068",
    ]

    try:

        # Launch browser and navigate to the website

        driver = open_browser(WEBSITE)

        # Enter survey code

        if not input_survey_code(driver, survey_code):
            raise Exception("Invalid Survey Code: Please check and try again.")

        print("Valid Survey Code")

        # 1: Please rate your overall satisfaction with your Panda Express experience.

        click_button(driver, "R000002." + rating)
        click_next(driver)

        # 1A: You selected that you were Highly Dissatisfied with your experience. Is this correct?

        if rating == "1":
            click_button(driver, "R000003.1")
            click_next(driver)

        # 1B: If NOT dine-in, please select your visit type:

        if visit_type == 1 or visit_type == 2:

            if visit_type == 1:
                # Online order pick-up
                click_button(driver, "R000005.4")
            else:
                # Delivery
                click_button(driver, "R000005.5")

            click_next(driver)

            # 1C: Where did you place your order?
            click_button(driver, "R000006.4")
            click_next(driver)

        # 2: Review quality of food

        give_review(driver, rating, food_options)
        give_review(driver, rating, food_options)

        # 4: Which best describes your primary reason for visiting Panda Express? (Check all that apply.)

        click_button(driver, "R000498")
        click_next(driver)

        # 5: Bad Review

        if rating == "1" or rating == "2" or rating == "3":
            while not driver.find_elements(By.ID, "textR000069"):
                for option in bad_review_options:
                    if driver.find_elements(By.ID, option):
                        click_button(driver, option)
                        break

                click_next(driver)

        # 6A: Did you have a problem during your experience?

        if rating == "1":
            click_button(driver, "R000069.1")
            click_next(driver)

            # 6B: We are sorry to hear you experienced a problem! Please tell us the primary cause of your problem.

            click_button(driver, "R000318.99")
            click_next(driver)

            # 6C: Please rate your satisfaction with how well the problem was resolved.
            # If you did not bring the problem to the team member's attention, select N/A.

            click_button(driver, "R000070.9")

        else:
            click_button(driver, "R000069.2")

        click_next(driver)

        # 7: Would recommend

        give_review(driver, rating, recommendation_options)

        while not find_text(driver, "S000057"):
            click_next(driver)

        # 8: Provide the user's email

        type_value(driver, "S000057", email)
        type_value(driver, "S000064", email)
        click_next(driver)

        # click_next(driver)

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

        pause()
        driver.quit()

        return "Success"

    except Exception as e:
        return e
