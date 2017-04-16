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
