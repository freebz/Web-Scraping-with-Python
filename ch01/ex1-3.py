from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.pythonscraping.com/pages/error.html")
except HTTPError as e:
    print(e)
    # null을 반환하거나, break 문을 실행하거나, 기타 다른 방법을 사용
else:
    # 이 프로그램을 계속 실행합니다. expect 절에서 return이나 break를 사용했다면
    # 이 else 절은 필요 없습니다.
    end
