import requests
from bs4 import BeautifulSoup

def get_exchange_rate(target1, target2):

    #헤더 추가. 헤더가 없으면 로봇이 접속한 것처럼 보임. 일반 브라우저를 이용하여 접속한 것처럼 보이게 함
    headers= {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }

    #requests 라이브러리로 사이트에 접속하여 응답값을 가져옴
    response = requests.get("https://kr.investing.com/currencies".format(target1, target2),headers=headers)
    #BeautifulSoup 라이브러리를 이용하여 html로 보기 값을 찾기 좋게 함
    content = BeautifulSoup(response.content, 'html.parser')
    #마지막 환율 정보 찾기
    #containers = content.find('span',{'data-test':'instrument-price-last'})
    containers = content.find('span', {'data-test': 'instrument-price-last'})
    #환율 정보 출력
    print(containers.text)


get_exchange_rate('usd','krw')
