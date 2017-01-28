# 3.2.1 전체 사이트에서 데이터 수집

# 제목은 항상 h1 태그 안에 있으며 h1 태그는 페이지당 하나만 존재합니다.
# 모든 바디 텍스트는 div#bodyContent 태그에 들어 있음.
# 더 명확하게 첫 번째 문단의 텍스트만 선택한다면 div#mw-content-text -> p로 첫 번째 문단 태그만 선택하는 편이 나을 수 있습니다.
# 편집 링크는 항목 페이지에만 존재합니다. 존재한다면 li#ca-edit -> span -> a 로 찾을 수 있습니다.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing something! No worries though!")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print("----------------\n"+newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks("")
