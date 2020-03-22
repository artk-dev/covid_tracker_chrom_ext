import requests
import json
import boto3
from boto3.dynamodb.conditions import Key
import datetime

import json

def lambda_handler(event, context):
    dynamo = boto3.resource('dynamodb')
    table = boto3.Table('covid_data_table')

    now = datetime.datetime.now()
    current_time = now.strftime('%Y%m%d%H%M%S')
    timeda = datetime.timedelta(days=1)
    oldest_time = current_time - timeda
    response = table.query(
        KeyConditionExpression=Key('timestamp').between(oldest_time, current_time),
        ScanIndexForward=False
    )
    covid_data=json.dumps(response['Items'][0])
    return {
        'statusCode': 200,
        'body': json.dumps(covid_data)
    }