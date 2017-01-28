# /wiki/<article_name> 형태인 위키백과 항목 URL을 받고, 링크된 항목 URL 목록 전체를 반환하는 getLinks 함수
# 시작 항목에서 getLinks를 호출하고 반환된 리스트에서 무작위로 항목 링크를 선택하여 getLinks를 다시 호출하는 작업을. 프로그램을 끝내거나 새 페이지에 항목 링크가 없을 때까지 반복하는 메인 함수

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a",
                    href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
