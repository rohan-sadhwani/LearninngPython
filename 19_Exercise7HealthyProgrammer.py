import datetime
import time
import schedule
from pygame import mixer


def dwater():
    mixer.init()
    mixer.music.load("19_water.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play(-1)
    ch = "error"
    while ch == "error":
        ch = input("\nEnter 'Drank' to Stop music : ")
        if ch == "Drank" or ch == "drank":
            mixer.music.stop()
            localt = time.asctime(time.localtime(time.time()))
            with open("19_log.txt", "a") as f:
                f.write(f"{localt} : Drinked Water\n")


def exeye():
    mixer.init()
    mixer.music.load("19_eye.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play(-1)
    ch = "error"
    while ch == "error":
        ch = input("\nEnter 'Eydone' to Stop music : ")
        if ch == "Eydone" or ch == "eydone" or ch == "EyDone":
            mixer.music.stop()
            localt = time.asctime(time.localtime(time.time()))
            with open("19_log.txt", "a") as f:
                f.write(f"{localt} : Eye Exercise Done\n")


def exwork():
    mixer.init()
    mixer.music.load("19_workout.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play(-1)
    ch = "error"
    while ch == "error":
        ch = input("\nEnter 'Exdone' to Stop music : ")
        if ch == "Exdone" or ch == "exdone" or ch == "ExDone":
            mixer.music.stop()
            localt = time.asctime(time.localtime(time.time()))
            with open("19_log.txt", "a") as f:
                f.write(f"{localt} : Workout Exercise Done\n")


schedule.every(30).minutes.do(exeye)
schedule.every(45).minutes.do(exwork)
schedule.every().hour.do(dwater)

tempam = datetime.datetime.now()
tt9am = tempam.replace(hour=9, minute=0, second=0, microsecond=0)
t9am = tt9am.strftime("%H:%M:%S")

temppm = datetime.datetime.now()
tt5pm = temppm.replace(hour=17, minute=0, second=0, microsecond=0)
t5pm = tt5pm.strftime("%H:%M:%S")

print("\n**************Welcome to Healthy Program**************")
print("This program will automatically remind you to :")
print("1.Do Eye exercise every 30 minutes\n2. Do workout every 45 minutes\n3. Drink water every 60 minutes")
print("This program also keeps log of your every activity")

while True:
    time.sleep(1)
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")

    if t9am < current_time < t5pm:
        schedule.run_pending()
    else:
        break
