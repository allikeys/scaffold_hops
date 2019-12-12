import requests
import xmltodict, json

def fetch_json(url):
    response = requests.get(url)
    if response.status_code != 200:
        data = {}
    else: 
        data = response.json()

    return data

def fetch_xml(url):
    response = requests.get(url)
    if response.status_code != 200:
        response.raise_for_status()
    else: 
        data = xmltodict(response.content, attr_prefix='')

    return json.loads(json.dumps(data))