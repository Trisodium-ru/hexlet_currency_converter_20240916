import requests

# Параметры по умолчанию.
URL = 'https://www.cbr-xml-daily.ru/daily_json.js' # Центральный банк Российской Федерации.
API_KEY = '' # Ключ не нужен.


# Загрузка валюты из внешней ссылки.
def get_actual_currencies() -> dict:
    url = URL + API_KEY
    response = requests.get(url)
    return response.json()['Valute']
