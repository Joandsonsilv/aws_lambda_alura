import json


def lambda_handler(event, context):
    print("Estou fazendo um Log:", event)

    return {
        "statusCode": 200,
        "body": json.dumps("Hello from Lambda!")
    }

print(lambda_handler)