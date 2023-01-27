import googletrans

translator= googletrans.Translator()

#dest: 번역될 문자의 언어, src: 번역할 문자의 언어 ( auto 생략 가능)
str1 ="행복하세요"
result1=translator.translate(str1, dest='en', src='auto')
print(f"행복하세요 => {result1.text}")

str2="I am happy"
result2=translator.translate(str2, dest='ko', src='auto')
print(f"I am happy => {result2.text}")
