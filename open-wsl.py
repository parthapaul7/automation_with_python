import pyautogui as pg

pg.sleep(1)

pg.keyDown("super")
pg.press('1')
pg.keyUp("super")

pg.sleep(3)
pg.write("wsl", interval=0.1)
pg.press('enter')
pg.sleep(4)
pg.write("cd ~",  interval=0.01)
pg.press('enter')
pg.sleep(0.5)
    
pg.write("cd files/learning", interval=0.01)
pg.press('enter') 
pg.sleep(0.5)
pg.write("code .", interval=0.01)
pg.press("enter")

#shifting to anoter desktop
pg.sleep(8)
pg.hotkey('ctrl','super','f4')
pg.sleep(0.5)
pg.hotkey('ctrl','super','d')
pg.sleep(0.5)
pg.hotkey('ctrl','super','left')
pg.sleep(0.5)
pg.hotkey('super','tab')
pg.sleep(1)
pg.moveTo(627,209,0.5)
pg.click(button='right')
pg.move(100,120,0.5)
pg.click()
pg.move(450,0,0.5)
pg.click()
pg.click()
pg.sleep(2)
print(" Done ")