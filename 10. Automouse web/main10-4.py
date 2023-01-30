import pyautogui
import time
import pyperclip

weather = ["서울 날씨","부산 날씨","진주 날씨","경남 고성 날씨","강원도 날씨"]

addr_x=1437
addr_y=234
start_x = 991
start_y = 251
end_x = 1647
end_y = 654

for i in weather:
    pyautogui.moveTo(addr_x,addr_y,0.2)
    pyautogui.click()
    time.sleep(0.5)

    pyperclip.copy(i)
    pyautogui.hotkey("ctrl","v")
    time.sleep(0.5)

    pyautogui.write(["enter"])
    time.sleep(1)


    #pyautogui.screenshot('10. Automouse web\\'+i+".png", region=(start_x,start_y,end_x-start_x,end_y-start_y))
