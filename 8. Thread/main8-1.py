# 쓰레드 사용 모듈
import threading
import time

def thread1():
    while True:
        print('쓰레드1 동작')
        time.sleep(1.0)

# 쓰레드 설정
t1 = threading.Thread(target = thread1)
t1.start()

while True:
    print("메인 동작")
    time.sleep(2.0)
