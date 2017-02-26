# CHAPTER 9 폼과 로그인 뚫기

# 9.1 파이썬 requests 라이브러리

# 9.2 기본적인 폼 전송

import requests
params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
r = requests.post("http://pythonscraping.com/files/processing.php", data=params)
print(r.text)
