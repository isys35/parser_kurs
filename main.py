import requests
from bs4 import BeautifulSoup as BS

URL = 'https://banki24.by/kurs/list/'
BANKS ={
    'Абсолютбанк': 26,
    'БСБ-Банк': 15,
    'Паритетбанк': 9,
    'Беларусбанк': 2,
    'ТК Банк': 33,
    'Белорусский Народный Банк': 6,
    'Идея Банк': 24,
    'ТехноБанк': 4,
    'Франсабанк': 18,
    'Белгазпромбанк': 14,
    'Банк Решение': 25,
    'ВТБ Беларусь': 5,
    'Белагропромбанк': 3,
    'МТБанк': 11,
    'БТА Банк': 22,
    'СтатусБанк': 19,
    'Белинвестбанк': 12,
    'Приорбанк': 10,
    'Альфа-Банк': 20,
    'Банк Дабрабыт': 1,
    'БПС-Сбербанк': 8
}
HEADERS = {
    'Host': 'banki24.by',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://banki24.by/',
    'X-Requested-With': 'XMLHttpRequest'
}


def get_kurs():
    kurs = {}
    for bank in BANKS:
        branches = []
        r = requests.get(URL + str(BANKS[bank]), headers=HEADERS)
        json = r.json()
        for el in json:
            branches.append({
                'address': BS(el[0], 'html.parser').text,
                'USD': [el[1], el[2]],
                'EUR': [el[3], el[4]],
                'RUB': [el[5], el[6]],
            })
        kurs[bank] = branches
    return kurs


if __name__ == '__main__':
     kurs = get_kurs()
     print(kurs)