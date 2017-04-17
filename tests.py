# 1. Ler os dados no XML
# 2. Criar uma estrutura de dados para armazenar items
# 3. Criar um método que converte uma lista de items em um estrutura JSON.

from unittest import TestCase, mock, skip
import xml2json


class XMLToJsonTest(TestCase):

    @mock.patch("xml2json.requests.get")
    def test_get_raw_data(self, mock_requests):
        xml2json.get_raw_data("any path")
        mock_requests.assert_called_with("any path")

    @mock.patch.object(xml2json, 'get_raw_data')
    def test_get_items(self, mock_get_raw_data):
        mock_get_raw_data.return_value = """
        <rss>
            <channel>
                <title>Prognoos Test</title>
                <item>
                    <title>item 1</title>
                </item>
                <item>
                    <title>item 2</title>
                </item>
                <item>
                    <title>item 3</title>
                </item>
            </channel>
        </rss>
        """
        items = xml2json.get_items()
        self.assertIsInstance(items, list)
        self.assertEqual(3, len(items))

    def test_format_price_testcase_0(self):
        price = xml2json.format_price("R$ 75,90")
        self.assertEqual("75.90", price)

    def test_format_price_testcase_1(self):
        price = xml2json.format_price("$ 75,90")
        self.assertEqual("75.90", price)

    def test_item_to_dict_expected_keys(self):
        expected_keys = [
            'id', 'name', 'url', 'img_url', 'description', 'price', 'priceSell',
            'category', 'categoryName', 'installmentValue', 'installmentQty',
            'locale', 'author', 'author_img', 'opcional_1', 'opcional_2'
        ]
        item = """
        <item>
            <g:id>128</g:id>
            <title>Bateria Compatível Positivo E4128Q-CD E412P-C</title>
            <link>
            http://prognoostest.commercesuite.com.br/informatica/bateria-compativel-positivo-e4128q-cd-e412p-c?parceiro=3322
            </link>
            <g:price>R$ 71,37</g:price>
            <g:shipping_weight>100 g</g:shipping_weight>
            <description>Bateria Compatível Positivo E4128Q-CD E412P-C</description>
            <g:google_product_category>2082</g:google_product_category>
            <g:image_link>
            https://images.tcdn.com.br/img/img_prod/454682/bateria_compativel_positivo_e4128q_cd_e412p_c_128_1_20160202222537.jpg
            </g:image_link>
            <g:product_type>Informática</g:product_type>
            <g:availability>in stock</g:availability>
            <g:sale_price_effective_date/>
            <g:identifier_exists>false</g:identifier_exists>
            <g:mpn>128</g:mpn>
            <g:installment>
                <g:months>7</g:months>
                <g:amount>R$ 11,02</g:amount>
            </g:installment>
            <g:condition>new</g:condition>
        </item>
        """
        item = xml2json.BeautifulSoup(item, 'lxml')
        dict_item = xml2json.item2dict(item)
        self.assertTrue(all(key in dict_item.keys() for key in expected_keys))

    @mock.patch.object(xml2json, 'get_items')
    @mock.patch.object(xml2json, 'item2dict')
    @skip("TODO: Test method generate_json")
    def test_generate_json(self, mock_item2dict, mock_get_items):
        # Recebe uma lista de items em formato bruto
        # Retorna uma string json.
        xml2json.generate_json()
        mock_get_items.assert_called_with()
