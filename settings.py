import api

# Количество полаченных конвертаций.
convertation_paid = 3

# Получаем данные из интернета по валютам.
# TODO Хранить только нужные данные в удобном формате.
currencies = api.get_actual_currencies()

# TODO Выбор основной валюты расчёта по умолчанию.
# На данный момент все расчёты относительно рубля, для российских пользователей.
currencies['RUB'] = {'Value': 1, 'Nominal': 1, 'CharCode': 'RUB', 'Name': 'Российский рубль'}

print(currencies)