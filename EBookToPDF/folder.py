import os
from tkinter import *
from tkinter import filedialog

#Create Window to select a target folder
def pathSelection():
    root = Tk()
    root.withdraw()
    root.update()
    folder_selected = filedialog.askdirectory()
    if folder_selected == "":
        print("Kein Ordner ausgewählt")
        exit()
    root.destroy()
    return folder_selected
