from bs4 import BeautifulSoup
import requests

def get_raw_data(path):
    resp = requests.get(path)
    return resp.text

def get_items():
    path = "http://prognoostest.commercesuite.com.br/xml/xml.php?Chave==A3boNXZsd2bvdGfygjN0UDN"
    raw_data = get_raw_data(path)
    soup = BeautifulSoup(raw_data, 'lxml')
    return soup.select('item')
