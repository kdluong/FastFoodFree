from panda import panda_express

# def main(event, context):


def main():

    option = 0  # panda express

    rating = "1"
    email = "kluong26@gmail.com"
    visit_type = 1  # 1: Online order pick-up, 2: Delivery
    survey_code = [1234, 1234, 1234, 1234, 1234, 12]

    if option == 0:
        response = panda_express(email, rating, visit_type, survey_code)

    print(response)


if __name__ == "__main__":
    main()
