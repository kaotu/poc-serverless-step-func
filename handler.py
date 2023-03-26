import json
import time


def hello(event, context):
    time.sleep(20)
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    print(response)

    return response

def good_bye(event, context):
    body = {
        "message": "👋 Good bye exit case!!!",
        "input": event
    }
    
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    
    print(response)
    return(response)