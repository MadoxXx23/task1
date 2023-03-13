import requests
from loguru import logger
from config import URL, CITY


def get_weather(places: list):
    params = {
        'lang': 'ru'
    }
    temp_list = []
    for place in places:
        req = requests.get(f"{URL}/{place}", params=params)
        if req.status_code == 200:
            temp_list.append(req.text)
        logger.error(f'Не удалось получить данные с сервера, т.к. код ответа сервера {req.status_code}')
    return temp_list


def main():
    weathers = get_weather(CITY)
    for weather in weathers:
        print(weather)
