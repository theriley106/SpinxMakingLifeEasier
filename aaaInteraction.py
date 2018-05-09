import requests

headers = {
		'pragma': 'no-cache',
		'origin': 'https://gasprices.aaa.com',
		'accept-encoding': 'gzip, deflate, br',
		'x-requested-with': 'XMLHttpRequest',
		'accept-language': 'en-US,es-US;q=0.8,es;q=0.6,ru-BY;q=0.4,ru;q=0.2,en;q=0.2',
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/60.0.3112.113 Chrome/60.0.3112.113 Safari/537.36',
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'accept': 'application/json, text/javascript, */*; q=0.01',
		'cache-control': 'no-cache',
		'authority': 'gasprices.aaa.com',
}



def getAverage(state):
	info = {}
	headers['referer'] = 'https://gasprices.aaa.com/?state={}'.format(state)
	data = [
		('action', 'states_cost_data'),
		('data[locL]', state),
		('data[locR]', 'US'),
	]
	response = requests.post('https://gasprices.aaa.com/wp-admin/admin-ajax.php', headers=headers, data=data)
	priceInfo = response.json()
	info['unleaded'] = {"state": priceInfo['data']['unleaded'][0], "country": priceInfo['data']['unleaded'][1]}
	info['midgrade'] = {"state": priceInfo['data']['midgrade'][0], "country": priceInfo['data']['midgrade'][1]}
	info['diesel'] = {"state": priceInfo['data']['diesel'][0], "country": priceInfo['data']['diesel'][1]}
	info['premium'] = {"state": priceInfo['data']['premium'][0], "country": priceInfo['data']['premium'][1]}
	return info
if __name__ == '__main__':
	print getAverage(raw_input("State: "))
