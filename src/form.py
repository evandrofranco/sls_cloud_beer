import os
import json
import boto3


def handler(event, context):

    print(event)

    token = os.environ.get('TOKEN')

    # Simple Token Validation
    if(event['headers']['Authorization'] != token):
        return {
            'statusCode': 401
        }

    # AWS Dynamo DB Object
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.getenv('TABLE_NAME'))

    # Get Request Values from Body
    body = json.loads(event['body'])

    # Create Dynamo Dict
    dynamo_values = {"name": body['name'], "email": body['email'],
                     "rate": body['rate'], "usage": body['usage'],
                     "knowledge": body['knowledge'],
                     "experience": body['experience'],
                     "comment": body['comment']}

    # Insert into Dynamo
    response = table.put_item(Item=dynamo_values)

    print(response)

    return {
        'statusCode': 200,
        'body': json.dumps({'msg': "OK"}),
        'headers': {'Access-Control-Allow-Origin': '*'}
    }
