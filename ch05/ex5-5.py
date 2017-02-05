# 5.3.3 파이선과의 통합

import pymysql
conn = pymysql.connect(host='127.0.0.1')

cur = conn.cursor()
cur.execute("USE scraping")
cur.execute("SELECT * FROM pages WHERE id=1")
print(cur.fetchone())
cur.close()
conn.close()
