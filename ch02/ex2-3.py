# 2.2.3 트리 이동

# 자식과 자손

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

for child in bsObj.find("table", {"id": "giftList"}).children:
    print(child)
