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

def format_price(string_price):
    # formatted_price = string_price.replace('R$ ', '').replace(',', '.')
    test_char = lambda c: c.isdigit() or c == ','
    formatted_price = "".join(c for c in string_price if test_char(c))
    return formatted_price.replace(',', '.')
