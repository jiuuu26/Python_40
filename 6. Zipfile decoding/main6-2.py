import itertools
import zipfile

passwd_string = "01234"

zFile=zipfile.ZipFile(r'6. Zipfile decoding\code1234.zip')

for len in range(1,6):
    #passwd_string 문자열을 repeat=길이로 정렬하여 반환
    to_attempt=itertools.product(passwd_string,repeat=len)
    #반환된 문자의 수만큼 반복
    for attempt in to_attempt:
        #반환된 값을 문자열로 반환. ''.join(리스트)는 리스트의 값을 문자열로 반환
        passwd=''.join(attempt)
        #print(passwd)
        try:
            zFile.extractall(pwd=passwd.encode())
            print(f'비밀번호는 {passwd}입니다.')
            break
        except:
            pass