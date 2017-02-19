# 8.2.1 위키백과의 여섯 다리: 결론

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connect(host='127.0.0.1', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute("USE wikipedia")

class SolutionFound(RuntimeError):
    def __init__(self, message):
        self.message = message

def getLinks(fromPageId):
    cur.execute("SELECT toPageId FROM links WHERE fromPageId = %s", (fromPageId))
    if cur.rowcount == 0:
        return None
    else:
        return [x[0] for x in cur.fetchall()]

def constructDict(currentPageId):
    links = getLinks(currentPageId)
    if links:
        return dict(zip(links, [{}]*len(links)))
    return {}

# 링크 트리가 비어 있거나 링크가 여러 개 들어 있습니다.
def searchDepth(targetPageId, currentPageId, linkTree, depth):
    if depth == 0:
        # 재귀를 중지하고 함수를 끝냅니다.
        return linkTree
    if not linkTree:
        linkTree = constructDict(currentPageId)
        if not link
