import requests

headers = {
    'Content-type': 'application/json',
    'access_token': 'f1b412b8-0d5e-4164-8045-d3cfc24796c2',
    'Host': 'restmws.fuelrewards.com',
    'User-Agent': 'Apache-HttpClient/UNAVAILABLE (java 1.4)',
}

response = requests.get('https://restmws.fuelrewards.com/fuelrewards/public/rest/cardbalance/cardnumber/782424421400826845/participantid/24270', headers=headers)

print(response.json())