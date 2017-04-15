import requests
from io import StringIO

def get_xml_data(path):
    resp = requests.get(path)
    return StringIO(resp.text)
