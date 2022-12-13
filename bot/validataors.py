import re

import lxml.etree
from lxml.etree import XPathSyntaxError


def str_is_xpath(xpath):
    """
    Валидация xpath
    """
    try:
        lxml.etree.XPath(xpath)
        return True
    except XPathSyntaxError:
        return False


def str_is_url(url: str):
    """
    Валидация URL
    """
    regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if re.match(regex, url):
        return True
    else:
        return False

# xpath1 = '//*[@id="react-root"]/section'
# xpath2 = '//*[@id="react-root"]/section[0]'
# print(str_is_xpath(xpath2))