import sqlite3

import msg
import pandas as pd
from validataors import str_is_url, str_is_xpath


def check_table_and_insert_data(file_path):
    """
    Проверяем содержимое таблицы загруженного файла.
    Name, URL, Xpath.
    При успешной проверке загружаем в db SQL.
    """
    report = ''
    title = ['name', 'url', 'xpath']
    d = pd.read_excel(file_path, header=None, names=title)
    lt = d.values.tolist()
    if len(lt[0]) != 3:
        return msg.msg_table_len()
    if len(lt[0]) == 3:
        for items in lt:
            name, url, xpath = items
            url_status = str_is_url(url=url)
            xpath_status = str_is_xpath(xpath=xpath)
            if url_status is False:
                report += f'{name} {msg.msg_table_url()}'
            if xpath_status is False:
                report += f'{name} {msg.msg_table_xpath()}'
        if report == '':
            try:
                con = sqlite3.connect('db.sqlite')
                table = d.to_string(
                    index=False, max_colwidth=30, justify='center')
                d.to_sql(
                    name='krakoz', con=con, if_exists='append', index=False)
                con.close()
                return {'table': table}
            except Exception as er:
                return msg.msg_file_error(er=er)
        else:
            return report
