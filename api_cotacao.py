import requests
import json
import time

while True:
    requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
    if requisicao:
        cotacao = json.loads(requisicao.text)
        print('1',cotacao['USD']['name'],'custa',cotacao['USD']['high'],'reais')
        time.sleep(10)