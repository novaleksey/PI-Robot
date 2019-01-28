import re
from urllib.parse import urlparse


def normalize_string(raw_string):
    res =raw_string.replace('\r', '').\
        replace('\t', '').\
        replace('\n', '').\
        strip(' ')
    return res


def parse_url(url):
    uri = urlparse(url)
    return f'{uri.scheme}://{uri.netloc}'


def parse_deposit(deposit):
    res = deposit.replace('.', '')
    numbers = [int(s) for s in res.split() if s.isdigit()]
    if len(numbers) > 0:
        return numbers[0]
    else:
        return 0


def getLinks(bs_object):
    links = []

    for link in bs_object.find_all('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))

    return links

