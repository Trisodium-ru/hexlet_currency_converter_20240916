import converter # Подключаем конвертер.
import settings # Подключаем настройки.

# Список существующих возможностей.
def get_events() -> dict:
    return {
        'help': 'вывести помощь',
        'balance': 'вывести баланс',
        'currencies': 'вывести все валюты',
        'convert': 'для старта конвертации валют',
        'great': 'вывод топ-3 самых дорогих валют',
        'exit': 'выйти из программы'
    }

# Старт обработки комманд.
def start():
    pass

# Вывод приветственного сообщения.
def greetings() -> None:
    print('Добро пожаловать в Конвертер Валют!\n')

    # Дополнительно выводим стандартный help.
    command_help()

# Вывод помощи.
def command_help() -> None:
    # Получаем список возможных команд.
    events = get_events()

    # Выводим все доступные возможности конвертера.
    print('Возможности конвертера:')
    i = 0
    for event, info in events.items():
        i += 1
        print(f'{i}. {event}: {info}')

# Пасхалка.
def easter_egg():
    print('🥚🐇🐾')
    print('Пасхалка пройдена! Вы нашли дополнительный выход из конвертера кроме exit :)')
    exit()

# Вывод баланса.
def command_balance() -> None :
    print(f'Ваш баланс конвертаций: {settings.convertation_paid}.\nКогда они закончатся - конвертировать нельзя.')

# Вывод существующих валют.
def command_currencies() -> None :
    print('Доступные валюты:')
    # Выводим все валюты построчно из словаря.
    for currency in settings.currencies.values():
        print(f'- {currency['CharCode']} [{currency['Value']} RUB] - {currency['Name']}')
    print('Все доступные валюты указаны выше ↑. Для конвертации введите: convert')

# Начало конвертации валют.
def command_convert() -> bool:
    # Проверка лимита конвертаций перед конвертацией.
    if settings.convertation_paid == 0:
        print('Ой, кажется, вы исчерпали лимит конвертаций. Ведьмаку заплатите чеканной монетой.')
        return False

    # Ожидине и проверка на исходную валюту.
    original_currency = input('1. Введите исходную валюту из списка: ').strip().upper()
    if not is_currency(original_currency):
        print('Исходная валюта должна быть выбрана из списка. Повторите попытку конвертации convert или вызовите справку help.')
        return False

    # Ожидине и проверка на результирующую валюту.
    result_currency = input('2. Введите результирующую валюту из списка: ').strip().upper()
    if not is_currency(result_currency):
        print('Результирующая валюта должна быть выбрана из списка. Повторите попытку конвертации convert или вызовите справку help.')
        return False

    # Ожидине и проверка на количество исходной валюты.
    original_amount = get_number(input('3. Введите количество исходной валюты: ').strip())
    if not original_amount:
        print('Количество исходной валюты должно быть целым числом или числом с плавающей точкой/запятой не равным нулю.')
        print('Повторите попытку конвертации convert или вызовите справку help.')
        return False

    # Проверка на отрицательное количество валюты.
    if original_amount < 0:
        print(f'Кажется, у вас закончились средства, так как {original_amount} {original_currency} выглядит как крЕдит, а не дЕбет :(')
        return False

    # Конвертация исходной валюты в результирующую.
    result_amount = converter.convert(original_currency, result_currency, original_amount, settings.currencies)

    # Снимаем 1 балл конвертации.
    settings.convertation_paid -= 1

    print(f'{original_amount} {original_currency} = {result_amount} {result_currency}')

# Проверка на валюту, и валюту из списка.
def is_currency(currency: str) -> bool:
    return currency.isalpha() and currency in settings.currencies.keys()

# Проверка что введено количество валюты.
def get_number(str_number: str) -> float:
    # Вводим результирующую переменную для возврата функции.
    value = 0

    # Сохраняем знак числа.
    sign = -1 if str_number[0] == '-' else 1

    # Если есть знак минуса берём срез строки без учёта минуса.
    if sign == -1:
        str_number = str_number[1:]

    # Заменяем запятые на точки, чтобы привести к одному типу дробные числа.
    str_number.replace(',', '.')

    # Разбиваем строку по точке, чтобы получить целые и дробные числа.
    number = str_number.split('.')

    # Проверяем разбитое число по точке.
    match len(number):
        case 1: # Если массив из 1 элемента - это целое число.
            return int(str_number) if str_number.isnumeric() else 0
        case 2: # Если 2 элемента в массиве - это дробное.
            if number[0].isnumeric() and number[1].isnumeric():
                value = int(number[0]) + int(number[1]) / 10 ** len(number[1])

    # Выводим число со знаком.
    return sign * value

# Вывод прощания.
def command_exit() -> None:
    print('Программа закрыта. Bye bye!')
    exit()

# Вывод неизвестной команды/события.
def unknown_event(event: str) -> None:
    print(f'Неизвестная команда "{event}". Попробуйте другую или воспользуйтесь командой help.')

# Вопрос о продолжении ввода.
def start_command(event: str) -> None:
    # Пропустим строку для красоты вывода.
    print(f'\n↓ ↓ ↓ Результат вашей команды {event} ниже ↓ ↓ ↓\n')

# Вопрос о продолжении ввода.
def end_command(event: str) -> None:
    # Пропустим строку для красоты вывода.
    print(f'\n↑ ↑ ↑ Результат вашей команды {event} выше ↑ ↑ ↑')
    print(f'\nХотите что-то ещё? Введите команду: ')

# Вывести топ 3 дорогие валюты.
def command_great() -> None:
    print('🏆 Топ-3 дорогие валюты')
    greatest = sorted(settings.currencies.values(), key = lambda d: d['Value'], reverse = True)[0:3]
    for great_currency in greatest:
        print(f'{great_currency['CharCode']} [{great_currency['Value']} RUB] - {great_currency['Name']}')
