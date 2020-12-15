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
    return f'Текушее время {time} \n' \
           f'Погода {location} is \n' \
           f'Температура {temperature} \n' \
           f'{state} \n' \
           f'Давление: {parse_data["current"]["pressure_mb"] * 0.75} mm\n' \
           f'Ветер: {parse_data["current"]["wind_kph"]} km/h, {wind}\n'


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
    pressure = data['forecast']['forecastday'][0]['hour'][12]['pressure_mb'] * 0.75
    wind = data['forecast']['forecastday'][0]['day']['maxwind_kph']
    return f'Дата {period} \n' \
           f'{state}\n' \
           f'Днем {max_temp}\n' \
           f'Вечером  {min_temp}\n' \
           f'Средняя температура {avg_temp}\n' \
           f'Скорость ветра {wind}\n' \
           f'Давление {pressure}'



def forecast(location):
    type_req = 'forecast'
    url = W_URL.format(type_req, KEY, location)
    url += '&days=3'  # 3 days that condition for free plan
    data = requests.get(url).json()
    date_list, temp_list, state_list = [], [], []
    temp = data['forecast']['forecastday']
    for i in range(3):
        date_list.append(temp[i]['date'])
        temp_list.append(temp[i]['day']['avgtemp_c'])
        state_list.append(temp[i]['day']['condition']['text'])
    return f"Прогноз на 3 дня в  {location}\n" \
           f"{date_list[0]}\nСредняя температура {temp_list[0]}С\n" \
           f"{state_list[0]}\n" \
           f"{date_list[1]}\nСредняя температура {temp_list[1]}С\n" \
           f"{state_list[1]}\n" \
           f"{date_list[2]}\nСредняя температура {temp_list[2]}С\n" \
           f"{state_list[2]}"


def smart_function(query):
    answer = query
    if '-h' in query:
        answer = history(query, query[-10:])
    elif '-f' in query:
        answer = forecast(query)
    else:
        answer = current_weather(query)
    return answer

