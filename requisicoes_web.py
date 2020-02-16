import requests
cabecalho = {'USER-AGENT': 'pintudo'}
try:
    req = requests.post('https://putsreq.com/6fCeNA6jOWSALoZhiK2g', 
    headers=cabecalho)
except Exception as e:
    print("ERROR código: ", e)
else:
    print(req.text)