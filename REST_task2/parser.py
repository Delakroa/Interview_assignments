import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4

URL = 'https://service.nalog.ru/addrno.html'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/96.0.4664.45 Safari/537.36', 'accept': '*/*'}


def get_html(url, params=None):
    """Отправляем get запрос"""
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    """Позволяет получить коллекцию элементов."""
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all()


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
        # print(html.text)
    else:
        print('Error')


parse()
# <input type="text" name="ifns" maxlength="4" id="ifns" data-is-multi-select="false" data-kind="TREE" class="txt-wide
# txt-set inp-std" data-dict="SOUN_ADDRNO_FL" style="visibility: hidden; position: absolute; width: 1px;">


# <input type="search" id="txtFilter" placeholder="Фильтр" class="hidden inp-std" style="display: inline-block;">


# <a class="chk checked" href="#">7840 - Межрайонная инспекция ФНС России №9 по Санкт-Петербургу</a>

# <ul class="ontop" id="uni_select_4" style="top: 36px; width: 669px; display: none;">
# <li data-index="0" data-code="" class=""><b></b></li><li data-index="1" data-code="40909000" class=""><b>
# </b>40909000 - муниципальный округ №78</li>
# <li data-index="2" data-code="40913000" class=""><b></b>40913000 - муниципальный округ Владимирский округ</li></ul>