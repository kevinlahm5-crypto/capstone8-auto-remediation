import json

def lambda_handler(event, context):
    print("Event received:", json.dumps(event))
    return {"status": "NON_COMPLIANT_RESOURCE_DETECTED"}