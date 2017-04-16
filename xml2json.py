from bs4 import BeautifulSoup
import requests

def get_raw_data(path):
    resp = requests.get(path)
    return resp.text
