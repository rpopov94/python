import json
import requests
from config import KEY, W_URL


def current_weather(location):
    type_req = 'current'
    url = W_URL.format(type_req, KEY, location)
    response = requests.get(url)
    if response.status_code != 200:
        print('city not found')
    parse_data = response.json()
    temperature = parse_data['current']["temp_c"]
    state = parse_data['current']['condition']['text']
    time = parse_data['location']['localtime']
    wind = parse_data['current']["wind_dir"]
    return f'Current time: {time} \n' \
           f'Weather of {location} is \n' \
           f'Temperature is: {temperature} \n' \
           f'State: {state} \n' \
           f'Pressure: {parse_data["current"]["pressure_mb"] * 0.750064} mm\n' \
           f'Wind: {parse_data["current"]["wind_kph"]} km/h, {wind}\n'


def history(location, period):
    type_req = 'history'
    url = W_URL.format(type_req, KEY, location)
    url += '&dt={}'.format(period)
    response = requests.get(url)
    data = response.json()
    temp = data['forecast']['forecastday'][0]['day']['avgtemp_c']
    return temp