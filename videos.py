import pyautogui as pg

# print(pg.position())
pg.sleep(10)
for i in range(0,100):
    pg.moveTo(370,713,1)
    pg.click(370,713)
    pg.moveTo(451,845,2)
    pg.sleep(2)
    pg.click(451,845)
    

print("finished")
