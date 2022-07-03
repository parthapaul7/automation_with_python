from cgi import print_arguments
import pyautogui as pg

size = pg.size()
position = pg.position()

print(size,position)
# pg.mouseDown(button='left')
# pg.moveTo(935,903,2)
# pg.mouseUp(button='left')