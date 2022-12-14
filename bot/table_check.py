import pandas as pd
import msg
import sqlite3
from validataors import str_is_url, str_is_xpath
# file_path = '/home/kirlx/Dev_lx/Parsing_bot/bot/tempfiles/file_33.xlsx'


def check_table(file_path):
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
    # else:
    if len(lt[0]) == 3:
        for items in lt:
            name, url, xpath = items
            url_status = str_is_url(url=url)
            xpath_status = str_is_xpath(xpath=xpath)
            if url_status is False:
                report += f'{name} {msg.msg_table_url()}'
            if xpath_status is False:
                report += f'{name} {msg.msg_table_xpath()}'
        #
        if report == '':
            try:
                # insert data in sql
                con = sqlite3.connect('db.sqlite')
                # rows = ['name', 'url', 'xpath']
                # d = pd.read_excel(file_path, header=None, names=rows)
                table = d.to_string(
                    index=False, max_colwidth=15, justify='center')
                d.to_sql(
                    name='krakoz', con=con, if_exists='append', index=False)
                con.close()
                return {'table': table}
            except Exception as er:
                return msg.msg_file_error(er=er)
        else:
            return report
            
    # con = sqlite3.connect('db.sqlite')
    # title = ['name', 'url', 'xpath']
    # xls, xlsx, xlsm, xlsb, odf, ods and odt
    # d = pd.read_excel(cloud_doc, header=None, names=title)
    # d.to_sql(name='krakoz', con=con, if_exists='append', index=False)
    # con.close()

    # no_indx = d.to_string(index=False, max_colwidth=50, justify='center')    
    # print(no_indx)
    #     name                        url                                       xpath               
    # OZON https://www.ozon.ru/search/?brand=26303000&from...            //span[@class="_32-a2"]


    # g = d.values.tolist()
    # for x in g:
    #     a, b, c = x
    #     print('URL=', a)
    #     print('XP=', c)
        #         URL= OZON
        # XP= //span[@class="_32-a2"]

# print(check_table(file_path))