#정규식 표현 사용
import re

#테스트용으로 사용할 문자열 생성. 문자열 여러개 입력하기 위해 """ 사용
test_string = """
aaa@bbb.com
123@abc.co.kr
test@hello.kr
ok@ok.co.kr
ok@ok.co.kr
no.co.kr
no.kr
"""

#문자열에서 이메일 형식 찾아 리스트 형태로 결과 반환
results = re.findall(r'[\w\.-]+@[\w\.-]+',test_string)

#set을 사용하여 중복 제거
results = list(set(results))

print(results)

