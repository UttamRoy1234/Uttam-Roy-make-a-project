from tkinter import *
import os

suraj_root = Tk()
suraj_root.geometry("1240x1050")

for root, dirs, files in os.walk("/img"):
    for file in files:
        if file.endswith(".png"):
            Label(image=PhotoImage(file=str(file))).pack()

suraj_root.mainloop()