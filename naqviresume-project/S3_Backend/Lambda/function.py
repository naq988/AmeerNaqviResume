import json
import boto3


def handler(event, context):
    dynamodb = boto3.client('dynamodb')
    try:
        response = dynamodb.get_item(TableName='naqviresumecounter', Key={'Site': {'N': '0'}})
        visits = int(response["Item"]["Visits"]["N"]) + 1
        dynamodb.put_item(TableName='naqviresumecounter', Item={
            'Site': {'N': '0'},
            'Visits': {'N': str(visits)}
        })
        return {
            'statusCode': 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "application/json",
                'Access-Control-Allow-Methods': '*',
                "Access-Control-Allow-Credentials": 'true'
            },'body': json.dumps(visits)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'error': str(e)
        }


