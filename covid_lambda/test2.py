import requests
import json

http_session = requests.Session()
http_session.trust_env = False
result = http_session.post('https://j1ryxp2q26.execute-api.eu-west-2.amazonaws.com/default/covidDataUpdater', data=json.dumps({"county":"Hampshire","query":"*"}), headers={'content-type': 'application/json'}, verify=False)
print(result.text)