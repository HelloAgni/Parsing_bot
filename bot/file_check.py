import pathlib

TEMP_DIR = '/tempfiles/'
EXTENSIONS = ['xls', 'xlsx', 'xlsm', 'xlsb', 'odf', 'ods', 'odt']


def check_extensions(file_name):
    """
    Перед скачиванием проверяем расширение файла.
    Пока осуществлена поддержка Excel файлов.
    """
    ext = file_name.split('.')[-1]
    print('Ext', ext)
    # 'xlsx'
    if ext not in EXTENSIONS:
        return False
    return True


def temp_file_path(doc):
    """
    Получаем имя файла и указываем путь для скачивания
    """
    file_name = doc['file_path'].split('/')[-1]
    print('F1', file_name)
    # F1 file_26.xlsx
    # file_name = 'file_26.xlsx'
    if check_extensions(file_name):
        current_dir = pathlib.Path(__file__).parent
        print('F2', str(current_dir))
        # F2 /home/kirlx/Dev_lx/Simple_bot1/tz_bot
        file_path = str(current_dir) + TEMP_DIR + file_name
        return file_path
    return False