from os import linesep
import googletrans

translator=googletrans.Translator()

read_file_path = r"9. Translation\english_file.txt"
write_file_path = r"9. Translation\korean_file.txt"

# 파일에서 줄별로 읽어 readlines에 리스트 형태로 바인딩
with open(read_file_path,'r') as f:
    readLines=f.readlines()

# 한 줄씩 한글로 변환
for lines in readLines:
    result1 = translator.translate(lines, dest='ko')
    print(result1.text)
    with open(write_file_path,'a',encoding='UTF8') as f:
        f.write(result1.text +'\n')