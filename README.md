# Desafio Cognitivo

## Questão 1
O Módulo xml2json implementa a conversão de um arquivo xml em json, conforme especificações da documentação.

### Uso
```shell
python3 xml2json.py <url_ou_path_do_xml>
```
Caso o caminho seja omitido, então a url utilizada será: http://prognoostest.commercesuite.com.br/xml/xml.php?Chave==A3boNXZsd2bvdGfygjN0UDN

## Questão 2
A estratégia adotada para esta questão foi a de ordenar o array de forma crescente e em seguida selecionar o primeiro elemento do array ordenado.
O método de ordenação escolhido foi o QuickSort, que tem complexidade espacial igual a log n.

Essa solução foi implementada no módulo quick_sort.py

## Ambiente

Todos os métodos foram testados em ambiente Unix (Linux / Debian 8) e python 3.5

O programa deve rodar com pouca ou nenhuma alteração em qualquer plataforma compatível com Python 3.x.

## Rodando os testes
```shell
python3 -m unittest
```
