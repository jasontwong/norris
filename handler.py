import json


def norris(event, context):
    body = {
        "message": "Chuck Norris is awesome!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
