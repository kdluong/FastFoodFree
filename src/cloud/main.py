import functions_framework
from panda import panda_express

@functions_framework.http
def hello_http(request):

    try:
        
        request_json = request.get_json(silent=True)
        request_args = request.args

        option = ""
        survey_code = []
        visit_type = 0
        email = ""
        rating = 1

        # fetch restaurant 

        if request_json and 'option' in request_json:
            option = request_json['option']
        else:
            raise Exception("Missing option.")

        # fetch survey code

        if request_json and 'survey_code' in request_json:
            survey_code = request_json['survey_code']
        else:
            raise Exception("Missing survey_code.")

        # fetch visit type 
        # 0: In-store, 1: Online Order, 2: Delivery

        if request_json and 'visit_type' in request_json:
            visit_type = request_json['visit_type']
        else:
            raise Exception("Missing visit_type.")

        # fetch email 

        if request_json and 'email' in request_json:
            email = request_json['email']
        else:
            raise Exception("Missing email.")
        
        # fetch rating 

        if request_json and 'rating' in request_json:
            rating = request_json['rating']
        else:
            raise Exception("Missing rating.")

        if option == "panda_express":
            response = panda_express(email, rating, visit_type, survey_code)
        else:
            raise Exception("Incorrect option")

        if response != "success":
            raise Exception(str(response))
        
        return {"statusCode": 200, "body": response}
        
    except Exception as e:
        return {"statusCode": 500, "body": str(e)}