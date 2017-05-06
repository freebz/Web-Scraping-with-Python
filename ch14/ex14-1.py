# CHAPTER 14 원격 스크레이핑

# 14.1 원격 서버를 쓰는 이유

# 14.1.1 IP 주소 차단 방지

# 14.1.2 이동성과 확장성

# 14.2 토르

# 14.2.1 파이삭스

import socks
import socket
from urllib.request import urlopen

socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket
print(urlopen('http://icanhazip.com').read())
