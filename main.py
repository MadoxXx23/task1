import requests


URL='https://wttr.in'
PLACES = ['Лондон', 'Череповец', 'SVO']
def get_weather(places: list):
    params = {
        'lang': 'ru',
        'n': '',
        'T': '',
        'q': ''

    }
    temp_list = []
    for place in places:
        req = requests.get(f"{URL}/{place}", params=params)
        if req.status_code == 200:
            temp_list.append(req.text)
        else:
            print(f'Не удалось получить данные с сервера, т.к. код ответа сервера {req.status_code}')
    return temp_list


def main():
    weathers = get_weather(PLACES)
    for weather in weathers:
        print(weather)

if __name__=="__main__":
    main()