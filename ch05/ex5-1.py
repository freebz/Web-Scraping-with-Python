# 5장 데이터 저장

# 5.1 미디어 파일

from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com")
bsObj= BeautifulSoup(html, "html.parser")
imageLocation = bsObj.find("a", {"id":"logo"}).find("img")["src"]
urlretrieve(imageLocation, "logo.jpg")
