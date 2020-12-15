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
           f'Pressure: {parse_data["current"]["pressure_mb"] * 0.75} mm\n' \
           f'Wind: {parse_data["current"]["wind_kph"]} km/h, {wind}\n'


def history(location, period):
    type_req = 'history'
    url = W_URL.format(type_req, KEY, location)
    url += '&dt={}'.format(period)
    response = requests.get(url)
    data = response.json()
    state = data['forecast']['forecastday'][0]['day']['condition']['text']
    max_temp = data['forecast']['forecastday'][0]['day']['maxtemp_c']
    avg_temp = data['forecast']['forecastday'][0]['day']['avgtemp_c']
    min_temp = data['forecast']['forecastday'][0]['day']['mintemp_c']
#    pressure = data['forecast']['forecastday'][0]['hour']['12']['pressure_mb'] * 0.75
    wind = data['forecast']['forecastday'][0]['day']['maxwind_kph']
    return f'For {period} \n' \
           f'State {state}\n' \
           f'Max temperature {max_temp}\n' \
           f'Min temperature {min_temp}\n' \
           f'Average temperature {avg_temp}\n' \
           f'Velocity wind {wind}\n' \
           f'Average pressure \n'


def forecast(location):
    type_req = 'forecast'
    url = W_URL.format(type_req, KEY, location)
    url += '&days=3'                            # 3 days that condition for free plan
    data = requests.get(url).json()
    date_list, temp_list, state_list = [], [], []
    temp = data['forecast']['forecastday']
    for i in range(3):
        date_list.append(temp[i]['date'])
        temp_list.append(temp[i]['day']['avgtemp_c'])
        state_list.append(temp[i]['day']['condition']['text'])
    return f"Forecast for three days in {location}\n" \
           f"{date_list[0]}\nAverage temp {temp_list[0]}\n" \
           f"State {state_list[0]}\n"\
           f"{date_list[1]}\nAverage temp {temp_list[1]}\n" \
           f"State {state_list[1]}\n" \
           f"{date_list[2]}\nAverage temp {temp_list[2]}\n" \
           f"State {state_list[2]}"


def smart_function(location, fore=None, hist=None, period=None):
    if fore is None and hist is None:
        return current_weather(location)
    elif fore == 'forecast' and hist is None:
        return forecast(location)
    else:
        return history(location, period)
