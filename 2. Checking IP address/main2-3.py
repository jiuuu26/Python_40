#컴퓨터 외부 IP 알아보는 코드 만들기

#사이트 접속을 위한 requests 모듈
#IP 주소를 찾기 위한 정규식을 사용하기 위해 re 모듈 사용
import requests
import re

req = requests.get("http://ipconfig.kr")
out_addr= re.search(r'IP ddress : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',req.text)[1]
print(out_addr)

