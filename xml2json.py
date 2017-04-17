from bs4 import BeautifulSoup
import requests
import json
import sys

class XMLToJson:

    def __init__(self, path=None):
        p = "http://prognoostest.commercesuite.com.br/xml/xml.php?Chave==A3boNXZsd2bvdGfygjN0UDN"
        self.path = path if path else p

    def get_raw_data(self, path):
        resp = requests.get(path)
        return resp.text

    def get_items(self, tag_name='item'):
        raw_data = self.get_raw_data(self.path)
        soup = BeautifulSoup(raw_data, 'lxml')
        return soup.select(tag_name)

    def format_price(self, string_price):
        # formatted_price = string_price.replace('R$ ', '').replace(',', '.')
        test_char = lambda c: c.isdigit() or c == ','
        formatted_price = "".join(c for c in string_price if test_char(c))
        return formatted_price.replace(',', '.')

    def item2dict(self, item):
        dict_item = {}
        dict_item['id'] = item.find("g:id").string
        dict_item['name'] = item.find("title").string
        dict_item['url'] = item.find("link").string
        dict_item['img_url'] = item.find("g:image_link").string
        dict_item['description'] = item.find("description").string
        dict_item['price'] = self.format_price(item.find("g:price").string)
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

    def generate_json(self):
        items = self.get_items()
        json_string = json.dumps(
            [self.item2dict(item) for item in items], ensure_ascii=False, indent=4
        )
        return json_string

def main():
    f = open('inventory.json', 'w')
    try:
        xml_to_json = XMLToJson(sys.argv[1])
    except IndexError:
        xml_to_json = XMLToJson()
    f.write(xml_to_json.generate_json())
    f.close()

if __name__ == '__main__':
    main()
