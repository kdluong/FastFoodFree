from panda import panda_express


def main(event, context):

    option = event["option"]
    survey_code = event["survey_code"]
    visit_type = event["visit_type"]
    email = event["email"]
    rating = event["rating"]

    # survey_code_1 = event["survey_code_1"]
    # survey_code_2 = event["survey_code_2"]
    # survey_code_3 = event["survey_code_3"]
    # survey_code_4 = event["survey_code_4"]
    # survey_code_5 = event["survey_code_5"]

    # survey_code = []
    # survey_code.append(survey_code_1)
    # survey_code.append(survey_code_2)
    # survey_code.append(survey_code_3)
    # survey_code.append(survey_code_4)
    # survey_code.append(survey_code_5)

    # option = "panda_express"  # panda express
    # rating = "1"
    # email = "kluong26@gmail.com"
    # visit_type = 1  # 1: Online order pick-up, 2: Delivery
    # survey_code = [1234, 1234, 1234, 1234, 1234, 12]

    response = None

    if option == "panda_express":
        response = panda_express(email, rating, visit_type, survey_code)

    if response != "success":
        return {"statusCode": 500, "body": response}

    return {"statusCode": 200, "body": response}


# if __name__ == "__main__":
#     main()
