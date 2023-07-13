import os
import time
from folder import pathSelection
import pyautogui
import fpdf
import pytesseract
from pdf2image import convert_from_path
import PyPDF2
import io
from ocr import *

fill = "------------------------------------------------------------------------------------------------------------------------"

print("Programm gestartet")
print(fill)
print("Wo soll die Datei erstellt werden?")

target = pathSelection()
screenshotFolder = target
screenshotFolderString = str(screenshotFolder)
screenshotCount = 0

pages = input("Wie viele Seiten hat das Dokument? ")
ausgabeName = input("Wie soll die Datei heissen? (ohne Leerschläge und Endung) ")
print(fill)

korr = input("Möchtest du die Koordinaten manuell eingeben? (j/n) ").lower()

if korr == "j":
    x = input("x (obere linke Ecke): ")
    y = input("y (obere linke Ecke): ")
    b = input("x (obere rechte Ecke): ")
    h = input("y (untere linke Ecke): ")
    width = int(b) - int(x)
    height = int(h) - int(y)
else:
    x = 1080 #Links oben x
    y = 380 #Links oben y
    height = 1640 #Höhe ab x
    width = 1170 #Breite ab y

def screenshot(selection):
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save(target + "/screenshot" + str(screenshotCount) + ".png")

print("In 5 Sekunden beginnt es, wechsle zum Bilschirm, den du aufnehmen möchtest")
print(fill)
time.sleep(5)

while screenshotCount < int(pages):
    screenshot([x, y, width, height])
    pyautogui.press("right")
    screenshotCount += 1
    time.sleep(1)

print("Möchtest du ein PDF erstellen? (j/n)")
pdf = input().lower()

if pdf == "j":
    print("Möchtest du OCR anwenden? (j/n)")
    ocr = input().lower()
    print(fill)

if pdf == "j" and ocr == "n":
    pdf = fpdf.FPDF()
    for i in range(0, screenshotCount):
        pdf.add_page()
        pdf.image(target + "/screenshot" + str(i) + ".png", 0, 0, 210, 297)
    pdf.output(target + "/" + ausgabeName + ".pdf", "F")
    print("PDF erstellt")

    #Löschen der Screenshots auf Windows
    if os.name == "nt":
        for i in range(0, screenshotCount):
            os.remove(target + "/screenshot" + str(i) + ".png")

    #Löschen der Screenshots auf Linux
    if os.name == "posix":
        for i in range(0, screenshotCount):
            os.system("rm " + target + "/screenshot" + str(i) + ".png")

    print("Screenshots gelöscht")
    
if pdf == "j" and ocr == "j": 
    try:
        ocr_funktion(screenshotFolderString, screenshotCount, ausgabeName)
    except:
        print("Stelle sicher, das Tesseract installiert ist oder frag Chrigu :)")
    
else:
    print("PDF nicht erstellt")

print("Programm beendet")