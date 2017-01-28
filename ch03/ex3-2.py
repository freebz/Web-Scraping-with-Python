# 항목링크와 다른링크 구분

# 이 링크들은 id가 bodyContent인 div 안에 있습니다.
# URL에는 세미콜론이 포함되어 있지 않습니다.
# URL은 /wiki/로 시작합니다.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html, "html.parser")
for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                      href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
