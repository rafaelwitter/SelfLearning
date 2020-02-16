import re

string_de_teste = 'Este eh o teste do teste dos fera do crack que faz os testinhos para ver se ok'
padrao = re.search(r'test.',string_de_teste)
if padrao:
    print(padrao.group())
else:
    print('nao foi encontrado.')
padron = re.findall(r'test\w*', string_de_teste)
if padron:
    print(padron)
else: 
    print("Nada")