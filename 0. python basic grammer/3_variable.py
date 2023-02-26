# ""안은 문자열, 문자와 숫자는 연산 불가 -> 형변환 필요 
a = 10
b = 20
d = "50"

c = a+b

# 문자를 숫자로 형변환 결과: 80
print(c+int(d))

# 숫자를 문자로 형변환 결과: 3050
print(str(c)+d)


# 정수와 실수형을 연산하면 자동 실수형으로 변환 -> 결과: 13.14
e= 3.14
print(a+e)


# 정수를 실수로 형변환 -> 결과: 30.0
f= float(a)+float(b)
print(f)

#type의 명령어로 타입 확인
a_bool=True
b_bool=False
a=1
b=0
# <class 'bool'>
print(type(a_bool))
print(type(b_bool))
# <class 'int'>
print(type(a))
print(type(b))
print(type(e))
