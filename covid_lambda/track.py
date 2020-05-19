import requests
import json
import boto3
import datetime

import json

def lambda_handler(event, context):
    body = event
    query = body['query']

    # Getting UK wide results
    result = requests.get('https://c19downloads.azureedge.net/downloads/data/data_latest.json')
    data = json.loads(result.text)

    ukcases = "N/A"
    newcases = "N/A"
    deaths = "N/A"

    for item in data['overview'].keys():
        dict1 = data['overview'][item]
        try:
            if dict1['name']['value'] == 'United Kingdom':
                ukcases = dict1['totalCases']['value']
                newcases = dict1['newCases']['value']
                deaths = dict1['deaths']['value']
                break
        except KeyError:
            continue
        except TypeError:
            continue

    totals = {"TotalUKCases":ukcases, "NewUKCases":newcases, "TotalUKDeaths":deaths}
    #========================
    result = requests.get('https://c19downloads.azureedge.net/downloads/data/utlas_latest.json')
    data = json.loads(result.text)

    #Adding a timestamp
    now = datetime.datetime.now()
    timestamp_simple = now.strftime('%Y%m%d%H%M%S')

    tracker_dict = {"timestamp":timestamp_simple}
    places = []

    #Restructuring data into a more legible format. Format: <county>:<total_cases>
    for item in data.keys():
        dict1 = data[item]
        try:
            county = dict1['name']['value']
            casecount = dict1['totalCases']['value']
            places.append(county)
            tracker_dict[county] = casecount
        except KeyError:
            continue

    places.sort()

    #------------------------------------------------------
    #--------getting case count----------------------------
    try:
            query_county = body['county']
    except KeyError:
        return {
            'statusCode': 200,
            'body': 'Invalid Request'
        }
    cases_result = None
    for key in tracker_dict.keys():
        if key == query_county:
            cases_result = tracker_dict[key]

    if cases_result==None:
        cases_result = "No data"
    #--------finished getting case count---------------------
    #--------------------------------------------------------

    if query=='places':
        return {
        'statusCode': 200,
        'body': json.dumps(places)
        }
    elif query == 'casecount':
        return {
            'statusCode': 200,
            'body': json.dumps(cases_result)
        }
    elif query=='totals':
        return {
            'statusCode': 200,
            'body': json.dumps(totals)
        }
    elif query=='*':
        totals.update({"places":places,"casecount":cases_result})
        return {
            'statusCode': 200,
            'headers':{
                'Access-Control-Allow-Origin':'*'
            },
            'body': json.dumps(totals)
        }
    else:
        return {
            'statusCode': 200,
            'body': 'Invalid Request'
        }