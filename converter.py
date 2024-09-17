# Конвертер валют.
def convert(original_currency: str, result_currency: str, original_amount: float, currencies: dict) -> float:
    # Получаем курс исходной и результирующей валюты.
    original_currency_value = currencies[original_currency]['Value']
    result_currency_value = currencies[result_currency]['Value']

    # Получаем коэфициент перевода исходной валюты в результирующую по их курсу.
    coefficient = original_currency_value / result_currency_value

    # Получаем итоговое количество конвертированной валюты.
    result_amount = coefficient * original_amount

    # Выводим результат с округлением до 2 занков после запятой.
    return round(result_amount, 2)
