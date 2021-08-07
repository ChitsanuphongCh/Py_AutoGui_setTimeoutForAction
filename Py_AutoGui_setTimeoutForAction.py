import pyautogui as pg
from time import sleep
from random import randint 
import datetime

pos = []
timeout = []
antiPauseScreen = False

while (True):
    print("Exit program input ( -1 )")
    position = input("Move mouse to postion and press ' ENTER ' : ")

    if position == '-1': break
    pos.append(pg.position().x)
    pos.append(pg.position().y)
    print("POSITION ( X , Y ) IS :", pos, "\n")
    
    now = datetime.datetime.now().strftime('%H:%M:%S:%d:%p').split(':')
    print(">> TIMENOW <<\nHOUR =", now[0], "\nMIN =", now[1], "\nSEC =", now[2], 
            "\nDAY =", now[3], "\nAM/PM ? =", now[4])

    showMsgInput = ["\nHOUR", "MIN", "SEC", "DAY", "AM / PM"]
    for i in range(len(showMsgInput)):
        timeout.append(input(showMsgInput[i] + " : "))
        if (i < len(showMsgInput)-1):
            timeout[i] = int(timeout[i])

    if(input("\nYou can random mouse position to anti pause screen ( Y/N ) : ") == 'Y'): 
        antiPauseScreen = True

    while (True):                              
        print()                          # HOUR : MIN : SEC : DAY : SEC
        now = datetime.datetime.now().strftime('%H:%M:%S:%d:%p').split(':')
        for i in range(len(now)-1):
            now[i] = int(now[i])
        
        if antiPauseScreen and now[2] % 20 == 0:  # RANDOM POSITION in 20s
            pg.moveTo(randint(0,pg.size()[0]), randint(0,pg.size()[1])) 
        if (now[0] >= timeout[0] and now[1] >= timeout[1] and now[2] >= timeout[2]
            and now[3] == timeout[3] and now[4] == timeout[4]):
            
            pg.moveTo(pos[0], pos[1])
            pg.click()
            pg.press('RETURN')
            break

        print("TIME NOW\t:", now)
        print("RUN START\t:", timeout)
        sleep(1)
    pos = []
    timeout = []
    