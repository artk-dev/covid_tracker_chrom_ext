import json
import requests
import boto3
import datetime

result = requests.get('https://c19downloads.azureedge.net/downloads/data/utlas_latest.json')
data = json.loads(result.text)

data_dict ={}
counties = []

for item in data.keys():
    dict1 = data[item]
    try:
        county = dict1['name']['value']
        casecount = dict1['totalCases']['value']
        counties.append(county)
        data_dict[county] = casecount
    except KeyError:
        continue

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

print(ukcases,newcases,deaths)