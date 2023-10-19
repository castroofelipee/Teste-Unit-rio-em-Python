import requests
import configparser


config = configparser.ConfigParser()
config.read('config.ini')
API_KEY = config['API']['key']


url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'


params = {
    'location': '37.7749,-122.4194',  
    'radius': '500',
    'type': 'restaurant',
    'key': API_KEY
}


response = requests.get(url, params=params)


if response.status_code == 200:
    data = response.json()
    for place in data['results']:
        print(place['name'], place['vicinity'])
else:
    print(f"A requisição falhou com o código de status {response.status_code}")
