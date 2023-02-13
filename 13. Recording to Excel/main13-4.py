#사이트에 접속하기 위한 모듈
import requests
import re
from openpyxl import load_workbook
from openpyxl import Workbook

url = 'https://n.news.naver.com/article/127/0000033674?cds=news_media_pc&type=editn'

#헤더 정보 입력. 하지 않을 시 로봇이 접속한 것으로 판단하여 응답하지 않는 사이트 많음
headers = {
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'text/html; charset=utf-8'
}

#url로 접속
response = requests.get(url, headers=headers)

#이메일 찾기
results = re.findall(r'[\w\.-]+@[\w\.-]+', response.text)

results = list(set(results))

print(results)

#email.xlsx 파일이 있어 읽어올 수 있다면 파일 읽기
try:
    wb = load_workbook(r"13. Recording to Excel\email.xlsx", data_only=True)
    sheet = wb.active

#email.xlsx 파일이 없다면 새로운 엑셀 생성
except:
    wb = Workbook
    sheet = wb.active

"""
#이메일을 수집한 수 만큼 반복
for result in results:
    sheet.append([result])
"""
wb.save(r"13. Recording to Excel\email.xlsx")
