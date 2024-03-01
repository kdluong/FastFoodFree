from panda import panda_express

# def main(event, context):

def main():

    option = 0

    rating = 1
    email = "kluong264@gmail.com"
    survey_code = [1234, 1234, 1234, 1234, 1234, 12]

    if option == 0:
        response = panda_express(email, rating, survey_code)

    print(response)

if __name__ == "__main__":
    main()