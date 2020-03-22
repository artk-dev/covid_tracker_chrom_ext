import requests
import json
import boto3
import datetime

import json

def lambda_handler(event, context):
    result = requests.get('https://services1.arcgis.com/0IrmI40n5ZYxTUrV/ArcGIS/rest/services/CountyUAs_cases/FeatureServer/0/query?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=GSS_NM%2CTotalCases&returnGeometry=false&returnCentroid=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=TotalCases&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pjson&token=')
    data = json.loads(result.text)
    features = data["features"]

    #Adding a timestamp
    now = datetime.datetime.now()
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
    timestamp_simple = now.strftime('%Y%m%d%H%M%S')

    print(timestamp_simple)

    tracker_dict = {"last_updated":timestamp,"timestamp":timestamp_simple}

    #Restructuring data into a more legible format. Format: <county>:<total_cases>
    for item in features:
        county = item['attributes']['GSS_NM']
        cases = item['attributes']['TotalCases']
        tracker_dict.update({county:cases})

    dynamo = boto3.resource('dynamodb',region_name='eu-west-2')
    table = dynamo.Table('covid_data_table')

    table.put_item(Item=tracker_dict)
    return {
        'statusCode': 200,
        'body': json.dumps('Covid data successfully updated!')
    }