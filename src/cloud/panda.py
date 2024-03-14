from operations import *

def input_survey_code(driver, survey_code):
    for index in range(0, 6):
        type_value(driver, "CN" + str(index + 1), survey_code[index])

    click_button(driver, "NextButton")    
    return not find_text_name(driver, "ErrorMessageOnTopOfThePage")

def click_next(driver):
    click_button(driver, "NextButton")

    if find_text_name(driver, "ErrorMessageOnTopOfThePage"):
        raise Exception("We have encountered an error. Please try again later. NEXT BUTTON")

def handle_button_click(driver, id, next):
    if find_text_id(driver, id):
        click_button(driver, id)

        if next:
            click_next(driver)
    else:
        raise Exception("We have encountered an error. Please try again later.")

def give_review(driver, rating, options):

    for option in options:
        if find_text_id(driver, option[0]):
            click_button(driver, option[1] + str(rating))

    click_next(driver)

def panda_express(email, rating, visit_type, survey_code):

    WEBSITE = "https://www.pandaguestexperience.com/Index.aspx?ADACompliance=true"

    FOOD_OPTIONS = [
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

    RECOMMENDATION_OPTIONS = [
        ("textR000074", "R000074."),
        ("textR000073", "R000073."),
        ("textR000141", "R000141."),
        ("textR000072", "R000072."),
    ]

    BAD_REVIEW_OPTIONS = [
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
            raise Exception("Invalid Survey Code")

        # 1: Please rate your overall satisfaction with your Panda Express experience.

        handle_button_click(driver, "R000002." + str(rating), True)

        if rating == 1:
            handle_button_click(driver, "R000003.1", True)
            
        # Check if visit type is correct

        visitCheck =  find_text_id(driver, "R000005.4")

        if visit_type > 0 and not visitCheck or visit_type == 0 and visitCheck:
            raise Exception("Invalid Order Option.")
        elif visit_type == 1 or visit_type == 2:
            
            # 1B: If NOT dine-in, please select your visit type:

            if visit_type == 1:
                # Online order pick-up
                click_button(driver, "R000005.4")
            else:
                # Delivery
                click_button(driver, "R000005.5")

            click_next(driver)

            # 1C: Where did you place your order?

            handle_button_click(driver, "R000006.4", True)

        # 2: Review quality of food

        give_review(driver, rating, FOOD_OPTIONS)
        give_review(driver, rating, FOOD_OPTIONS)

        # 3: Which best describes your primary reason for visiting Panda Express? (Check all that apply.)

        handle_button_click(driver, "R000498", True)

        # 4: Bad Review

        if rating < 4:
            while not find_text_id(driver, "textR000069"):
                for option in BAD_REVIEW_OPTIONS:
                    if find_text_id(driver, option):
                        click_button(driver, option)
                        break

                click_next(driver)

        # 5A: Did you have a problem during your experience?

        if rating == 1:

            handle_button_click(driver, "R000069.1", True)

            # 5B: We are sorry to hear you experienced a problem! Please tell us the primary cause of your problem.

            handle_button_click(driver, "R000318.99", True)

            # 5C: Please rate your satisfaction with how well the problem was resolved.
            # If you did not bring the problem to the team member's attention, select N/A.

            handle_button_click(driver, "R000070.9", False)

        else:

            handle_button_click(driver, "R000069.2", False)

        click_next(driver)

        # 6: Would recommend

        give_review(driver, rating, RECOMMENDATION_OPTIONS)

        while not find_text_name(driver, "S000057"):
            click_button(driver, "NextButton")

        # 7: Provide the user's email

        type_value(driver, "S000057", email)
        type_value(driver, "S000064", email)
        click_next(driver)

        # Terminate browser

        driver.quit()

        return "Success!"

    except Exception as e:

        if str(e) == "Invalid Survey Code":
            return "Invalid Survey Code: Please check and try again."

        return str(e)