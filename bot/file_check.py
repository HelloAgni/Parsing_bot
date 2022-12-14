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
    if ext in EXTENSIONS:
        return True
    return False


def check_file(doc):
    """
    Проверка расширения файла.
    Получение имени файла и указываем путь для скачивания.
    """
    file_name = doc['file_path'].split('/')[-1]
    print('F1', file_name)
    # F1 file_26.xlsx
    # file_name = 'file_26.xlsx'
    if check_extensions(file_name):
        current_dir = pathlib.Path(__file__).parent
        print('F2', str(current_dir))
        # F2
        file_path = str(current_dir) + TEMP_DIR + file_name
        return file_path
    return False
