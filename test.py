import requests
import main
import json
a = main.spinxAPI()
DATABASE = {}

for key, value in a.Data.items():
    try:
        headers = {
            'X-Parse-OS-Version': '7.1.1',
            'X-Parse-App-Build-Version': '240',
            'X-Parse-Client-Key': 'jnkI7Gc5FAjL6LuhqIQPayJOfLNmL2fd21DzanqG',
            'X-Parse-App-Display-Version': '2.4',
            'X-Parse-Client-Version': 'a1.14.1',
            'X-Parse-Installation-Id': 'a9cbabdc-c8dc-4e6f-8f7f-6d17e820d13d',
            'User-Agent': 'Parse Android SDK 1.14.1 (com.myspinx/240) API Level 25',
            'X-Parse-Application-Id': 'r1yw9lSfUdfcglpvPtODbvgQkPaHj6Faf5P1CmzM',
            'Content-Type': 'application/json',
            'Host': 'parseapi.back4app.com',
        }

        data = '{"where":"{\\"store_number\\":\\"119\\"}","_method":"GET"}'.replace('119', str(key))

        response = requests.post('https://parseapi.back4app.com/classes/Store', headers=headers, data=data)
        DATABASE[key] = response.json()['results'][0]
    except Exception as exp:
        print exp
        print("Failed on {}".format(key))

with open('data.json', 'w') as outfile:
    json.dump(DATABASE, outfile)