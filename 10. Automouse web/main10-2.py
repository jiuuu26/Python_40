import pyautogui
import time
import pyperclip

# 0.2초 동안 해당 좌표로 이동
pyautogui.moveTo(1437,234,0.2)
pyautogui.click()
# 0.5초 기다리기
time.sleep(0.5)

# 클립보드에 "서울 날씨 저장"
pyperclip.copy("서울 날씨")
# ctrl-v 키 입력
pyautogui.hotkey("ctrl","v")
# 0.5초 기다리기
time.sleep(0.5)

# 엔터키 입력
pyautogui.write(["enter"])
time.sleep(1)
