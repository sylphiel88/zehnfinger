import tkinter as tk
from tkinter import *
from tkinter import Tk
import random
import sys
import time

currtime = time.time()
pretime = time.time() - 1
currpos = 0
errors = 0
window = tk.Tk();
window.title('10Finger')
window.geometry("800x400+500+150")

string = ""
sammlung = "abcdefghijklmnopqrstuvwxyz"

apma = []
apm = 0

for i in range(random.randint(20, 30)):
    for j in range(random.randint(4, 8)):
        string += sammlung[random.randint(0, 25)]
    string += " "

tiplabel = Text(window, height=1, width=70, font=("Helvetica", 14))
tiplabel.insert("1.0", string)
tiplabel.tag_add("pos", "1.0")
tiplabel.tag_config("pos", background="yellow")
tiplabel.place(x=10, y=100)

errorLabel = Label(window, text="Errors: 0, APM= 0/min")
errorLabel.place(x=10, y=150)


def key_pressed(event):
    global string, currpos, tiplabel, currtime, pretime, errors, errorLabel, apma, apm
    if event.char == string[currpos] and not event.keysym == "Shift_L":
        currtime = time.time()
        apm = (60 / (currtime - pretime))
        pretime = currtime
        apma.append(apm)
        apm = sum(apma) / len(apma)
        apm = int(apm)
        string = string.replace(string[currpos], " ", 1)
        string += " "
        tiplabel.delete("1.0")
        currpos += 1
        tiplabel.tag_add("pos", "1.0")
        tiplabel.tag_config("pos", background="yellow")
        errorLabel.config(text="Errors: " + str(errors) + ", APM= " + str(apm) + "/min")
    elif not event.keysym == "Shift_L":
        errors += 1
        errorLabel.config(text="Errors: " + str(errors) + ", APM= " + str(apm) + "/min")
    if len(string.replace(" ", "")) == 0:
        print(apm)
        sys.exit()


window.bind("<Key>", key_pressed)

window.mainloop()