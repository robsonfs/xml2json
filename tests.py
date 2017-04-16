# 1. Ler os dados no XML
# 2. Criar uma estrutura de dados para armazenar items
# 3. Criar um método que converte uma lista de items em um estrutura JSON.

from unittest import TestCase, mock
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
