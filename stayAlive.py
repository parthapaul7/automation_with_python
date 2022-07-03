import pyautogui as pg

activeTime = int(input('How long do you want to be active in minutes?\n'))

for i in range(activeTime*60//10):
    pg.press('super')
    pg.sleep(3)  
    pg.press('super')
    pg.sleep(2)
    pg.move(100,0,1)
    pg.move(-100,0,1)
    pg.sleep(3)

print('finished in ' + str(activeTime) + 'minute')