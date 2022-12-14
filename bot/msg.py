def msg_hi(name):
    """
    Сообщение - приветствие Бота при активации /start.
    """
    return (f'Спасибо, что включили меня {name}\n'
            f'Я умею собирать данные о товарах\n'
            f'И выводить среднюю цену по указанным параметрам\n'
            f'Перенесите Excel файл в окно '
            f'чата или прикрепите нажав \U0001f4ce'
            )


def msg_stop():
    """
    Сообщение - системная остановка бота /stop.
    """
    return 'Бот отключен'


def msg_upload(data):
    """
    Сообщение - успешная загрузка данных.
    """
    return (f'Загружены следующие данные: \n{data}\n'
            f'Подождите, идет сбор информации...')


def msg_file_error(er):
    """
    Сообщение - ошибка загрузки файла.
    """
    return f'Похоже с файлом что-то не так: \n{er}'


def msg_file_check_error():
    """
    Сообщение - файл не прошел проверку поддерживаемых расширений.
    """
    return ('На данный момент поддерживаются только Excel файлы:\n'
            '.xls .xlsx .xlsm .xlsb .odf .ods .odt')


def msg_table_len():
    """
    Сообщение, что в таблице не 3 столбца.
    Name, URL, Xpath
    """
    return ('В таблице должно быть 3 столбца\n'
            'Name, URL, Xpath')


def msg_table_url():
    """
    Сообщение - url в таблице не валидный.
    """
    return '- URL не прошел проверку\n'


def msg_table_xpath():
    """
    Сообщение - xpath в таблице не валидный.
    """
    return '- Xpath не прошел проверку\n'


def msg_tolong_pars():
    """
    Сообщение - загрузка данных заняло много времени.
    """
    return 'Долго парсим...'


def msg_time_pars():
    """
    Сообщение - время за которое проверены данные.
    """
    return 'Данные загружены за '
