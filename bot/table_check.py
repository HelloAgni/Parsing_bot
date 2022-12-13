import pandas as pd
# import sqlite3
from validataors import str_is_url, str_is_xpath
# file_path = '/home/kirlx/Dev_lx/Parsing_bot/bot/tempfiles/file_33.xlsx'


def check_table(file_path):
    """
    Проверяем содержимое таблицы из облака.
    Name, URL, Xpath
    """
    report = ''
    title = ['name', 'url', 'xpath']
    # xls, xlsx, xlsm, xlsb, odf, ods and odt
    # d = pd.read_excel(file_path, header=None, names=title)
    d = pd.read_excel(file_path, header=None, names=title)
    lt = d.values.tolist()
    if len(lt[0]) != 3:
        return 'В таблице должно быть 3 столбца'
    else:
        for items in lt:
            name, url, xpath = items
            url_status = str_is_url(url=url)
            xpath_status = str_is_xpath(xpath=xpath)
            if url_status is False:
                report += f'{name} - URL не прошел проверку\n'
            if xpath_status is False:
                report += f'{name} - Xpath не прошел проверку\n'
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