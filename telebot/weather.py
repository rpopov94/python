import json
import requests
import config


def parse_weather_data(data):
    for elem in data['weather']:
        weather_state = elem['main']
    temp = round(data['main']['temp'] - 273.15, 2)
    city = data['name']
    msg = f'The weather in {city}: Temp is {temp}, State is {weather_state}'
    return msg


def get_weather(location):
    url = config.WEATHER_URL.format(city=location,
                                   token=config.WEATHER_TOKEN)
    response = requests.get(url)
    if response.status_code != 200:
        return 'city not found'
    data = json.loads(response.content)
    return parse_weather_data(data)
