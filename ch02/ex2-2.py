# 2.2 다시 BeautifulSoup

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())

# 문서의 모든 헤더 태그 리스트를 반환
bsObj.findAll({"h1", "h2", "h3", "h4", "h5", "h6"})

# 문서에서 녹색과 빨간색 span 태그를 모두 반환
bsObj.findAll("span", {"class":{"green", "red"}})

# 속성이 아닌 텍스트 콘텐츠에 일치하는 항목 찾기
nameList = bsObj.findAll(text="the prince")
print(len(nameList))

# 특정 속성이 포함된 태그를 선택
allText = bsObj.findAll(id="text")
print(allText[0].get_text())
