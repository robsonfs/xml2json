# 1. Ler os dados no XML
# 2. Criar uma estrutura de dados para armazenar items
# 3. Criar um método que converte uma lista de items em um estrutura JSON.

from unittest import TestCase, mock
import xml2json
from io import StringIO
import requests

class XMLToJsonTest(TestCase):

    @mock.patch("xml2json.requests.get")
    def test_get_xml_data(self, mock_requests):
        xml2json.get_xml_data("any path")
        mock_requests.assert_called_with("any path")
