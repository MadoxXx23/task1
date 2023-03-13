import requests
from config import URL, CITY


def get_weather(places: list):
    params = {
        'lang': 'ru'
    }
    temp_list = []
    for place in places:
        temp_list.append(requests.get(f"{URL}/{place}", params=params).text)
    return temp_list


def main():
    weathers = get_weather(CITY)
    for weather in weathers:
        print(weather)
