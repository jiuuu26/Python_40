# "",'' 모두 가능
print("hello")
print('hello')


# ,는 자동 띄어쓰기, +는 자동 띄어쓰기 X
print('안녕','하세요')
print('안녕'+'하세요')


# '''사용시 작성하는 대로 줄 바꿈
print('''안녕하세요
오늘은 날씨가 좋네요''')


# \ (역슬래쉬) 줄바꿈 -> 실제 한 줄을 코드의 가독성을 위해 코드에서만 띄울 때
print('안녕하세요'\
    '오늘은 날씨가 좋네요')


# .format 형식
a=123
b='hello'
print("a값:{} b값:{}" .format(a,b))


# f-string 형식
a=123
b='hello'
print(f'a값:{a}, b값:{b}')