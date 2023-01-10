import requests
import json
import sys


def search_clima(city):
    request = requests.get(f"https://api.hgbrasil.com/weather?key=8f56125c&city_name={city}")
    data = json.loads(request.content)
    city_name = data['results']['city_name']
    forecast = data['results']['forecast']
    print('Cidade: ' + city_name + '\n')
    
    for i in forecast:
        print('Data: ' + i ['date'])
        print('Dia da semana: ' + i ['weekday'])
        print('Máxima: ' + str(i['max']) + '°')
        print('Mínima: ' + str(i['min']) + '°')
        print('Previsão: ' +  i['description'] + '\n')


if __name__ == '__main__':
    param = sys.argv[1:]
    search_clima(param)
