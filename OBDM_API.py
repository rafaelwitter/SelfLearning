#!/usr/bin/python3.6
__author__ = 'Rafael Witt'
import requests
import json

def requisacao(titulo):
    try:
        req = requests.get('http://omdbapi.com/?t=' + titulo)
        dic = json.loads(req.text)
        return dic
    except Exception as e:
        print('ERRO')
        return None
    
def main(): 
    """
    Description
    :raises:
   
    :rtype:
    """
    sair = True
    while sair:
        titulo = input('Escreva o nome do filme ou SAIR para fehcar: ')
        if titulo == str.upper('SAIR'):
            sair = False
        else:
            filme = requisacao(titulo)
            if filme['Response'] == 'False':
                print('Nao encontrado esse filme.')
            else: print(filme)
main()
