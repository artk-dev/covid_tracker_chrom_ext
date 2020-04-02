import requests
import json
import boto3
import datetime

import json

def lambda_handler(event, context):
    body = event
    query = body['query']

    result = requests.get('https://services1.arcgis.com/0IrmI40n5ZYxTUrV/ArcGIS/rest/services/CountyUAs_cases/FeatureServer/0/query?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=GSS_NM%2CTotalCases&returnGeometry=false&returnCentroid=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=TotalCases&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pjson&token=')
    data = json.loads(result.text)
    features = data["features"]

    result2 = requests.get('https://services1.arcgis.com/0IrmI40n5ZYxTUrV/arcgis/rest/services/DailyIndicators/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outSR=102100&resultOffset=0&resultRecordCount=50&cacheHint=true')
    data2= json.loads(result2.text)
    data2=data2['features'][0]['attributes']
    totals = {"TotalUKCases":data2["TotalUKCases"],"NewUKCases":data2["NewUKCases"],"TotalUKDeaths":data2["TotalUKDeaths"]}
    #Adding a timestamp
    now = datetime.datetime.now()
    timestamp_simple = now.strftime('%Y%m%d%H%M%S')

    tracker_dict = {"timestamp":timestamp_simple}
    places = []

    #Restructuring data into a more legible format. Format: <county>:<total_cases>
    for item in features:
        county = item['attributes']['GSS_NM']
        cases = item['attributes']['TotalCases']
        tracker_dict.update({county:cases})
        places.append(county)
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