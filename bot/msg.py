def msg_hi(name):
    """
    Приветствие Бота при активации /start
    """
    return (f'Спасибо, что включили меня {name}\n'
            f'Перенесите Excel файл в окно '
            f'чата или прикрепите нажав \U0001f4ce'
            )


def msg_stop():
    """
    Системная остановка бота /stop
    """
    return 'Бот отключен'


def msg_upload(data):
    """
    Загрузка данных
    """
    return f'Загружены следующие данные: \n{data}'


def msg_file_error(er):
    """
    Ошибка загрузки файла
    """
    return f'Похоже с файлом что-то не так: \n{er}'


def msg_file_check_error():
    """
    Файл не прошел проверку поддерживаемых расширений
    """
    return ('На данный момент поддерживаются только Excel файлы:\n'
            '.xls .xlsx .xlsm .xlsb .odf .ods .odt')
