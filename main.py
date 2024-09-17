import commands

# Получаем возможный функционал.
events = commands.get_events()

# Изначально приветствуем и выводим инструкцию.
commands.greetings()

# MAIN. Тело бесконенчой программы.
while event := input().strip().lower(): # Получаем пользовательский ввод с очисткой пробелов.
    if event in events:
        # Вывод перед запуском команды.
        commands.start_command(event)

        # Запуск команды.
        # Вызов соответствующей команды c префиксом command_ из библиотеки commands.
        getattr(commands, 'command_'+event)()

        # Вывод после окончания команды.
        commands.end_command(event)
    else:
        commands.unknown_event(event)
else:
    commands.easter_egg()