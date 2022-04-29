import requests
import json
from jsonpath_ng import jsonpath, parse

#headers = {
#    'Content-type': 'application/json',
#}

def token_create ():
	response = requests.post('http://localhost/api/deneme/user/token/', auth=('admin', 'sandboxtt'))
	if response.status_code != 200:
		print ("İstek geçersiz, bilgileri kontrol ediniz.")
		return response.status_code;
	else:
		resp = response.text

		sonuc = json.loads(resp)

		jsonpath_expr = parse('$.data.token')

		parseFilter = jsonpath_expr.find(sonuc)
	
		token = parseFilter[0].value
	
		return token;

token_result = str(token_create())

token_headers = {
    'phpipam-token': token_result,
}
def ipcreate():
	response = requests.post('http://localhost/api/deneme/addresses/first_free/2', headers=token_headers)
	resp = response.text
	sonuc = json.loads(resp)	
	if response.status_code != 201:
		jsonpath_expr = parse('$.message')
		parseFilter = jsonpath_expr.find(sonuc)
		ipAdd = parseFilter[0].value
		return ipAdd;
	else:
		jsonpath_expr = parse('$.data')
		parseFilter = jsonpath_expr.find(sonuc)
		ipAdd = parseFilter[0].value
		return ipAdd;

ip_result = str(ipcreate())
        
print(ip_result)
