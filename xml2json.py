from bs4 import BeautifulSoup
import requests
import json

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

def item2dict(item):
    dict_item = {}
    dict_item['id'] = item.find("g:id").string
    dict_item['name'] = item.find("title").string
    dict_item['url'] = item.find("link").string
    dict_item['img_url'] = item.find("g:image_link").string
    dict_item['description'] = item.find("description").string
    dict_item['price'] = format_price(item.find("g:price").string)
    dict_item['priceSell'] = ""
    dict_item['category'] = item.find("g:google_product_category").string
    dict_item['categoryName'] = item.find("g:product_type").string
    dict_item['installmentValue'] = []
    dict_item['installmentQty'] = []
    dict_item['locale'] = ''
    dict_item['author'] = ''
    dict_item['author_img'] = ''
    dict_item['opcional_1'] = ''
    dict_item['opcional_2'] = ''

    return dict_item

def generate_json():
    items = get_items()
    json_string = json.dumps(
        [item2dict(item) for item in items], ensure_ascii=False, indent=4
    )
    return json_string
