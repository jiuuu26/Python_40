import pyautogui
import time
import pyperclip

    #Point(x=991, y=251) Point(x=1647, y=654)


pyautogui.moveTo(1437,234,0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("진주 날씨")
pyautogui.hotkey("ctrl","v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

start_x = 991
start_y = 251
end_x = 1647
end_y = 654

# 스크린샷을 찍어 weather.png에 저장
# region =(시작좌표 x, 시작좌표 y, 크기 x, 크기 y)
pyautogui.screenshot(r'10. Automouse web\weather.png', region=(start_x,start_y,end_x-start_x,end_y-start_y))