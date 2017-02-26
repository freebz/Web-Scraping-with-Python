# 9.3 라디오 버튼, 체크박스, 기타 필드

# 9.4 파일과 이미지 전송

import requests
files = {'uploadFile': open('./files/Python-logo.jpg', 'rb')}
r = requests.post("http://pythonscraping.com/pages/processing2.php",
                  files=files)
print(r.text)
