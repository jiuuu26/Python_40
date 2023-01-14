import random

#임의의 숫자 생성 코드 만들기
random_number= random.randint(1,100)


"""숫자가 아닌 다른 것(문자)를 입력했을 때 
프로그램이 종료되지 않도록 try except 구문 사용"""

game_count = 1

while True:
    try:
        my_number=int(input("1~100 사이의 숫자를 입력하세요:"))

        if my_number > random_number:
            print("다운")
            game_count+=1
        elif my_number < random_number:
            print("업")
            game_count+=1
        else:
            print(f"축하합니다. {game_count}회만에 맞췄습니다.")
            break
    except:
        print("에러가 발생하였습니다. 숫자를 입력하세요")
