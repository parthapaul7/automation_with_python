from pywinauto.application import Application
import time
from sys import exit

app = Application(backend="uia").start(r"C:\Users\Administrator\AppData\Local\Programs\Hyper\hyper.exe")

time.sleep(2)
app.Hyper.type_keys("wsl {ENTER}")
time.sleep(5)
app.Hyper.type_keys("cd {SPACE}~{ENTER}")
time.sleep(1)
app.Hyper.type_keys("cd {SPACE}files/learning{ENTER}")
time.sleep(1)
app.Hyper.type_keys("code {SPACE}. {ENTER}")
print("Done")

exit()