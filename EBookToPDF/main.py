import time

import fpdf
import pyautogui

from folder import pathSelection
from ocr import *

fill = "---------------------------------------------------------------------------------------------------------------"

print("Start...")
print(fill)
print("Where should the file be created?")

target = pathSelection()
screenshotFolder = target
screenshotFolderString = str(screenshotFolder)
screenshotCount = 0

pages = input("How many pages does the document have? ")
ausgabeName = input("What should the file be called? (without spaces and extension) ")
print(fill)

x = input("x (upper left corner): ")
y = input("y (upper left corner): ")
b = input("x (upper right corner): ")
h = input("y (lower left corner): ")
width = int(b) - int(x)
height = int(h) - int(y)


def screenshot(selection):
    screenshot: object = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save(target + "/screenshot" + str(screenshotCount) + ".png")


print("Starts in 5 seconds, switch to the screen you want to capture")
print(fill)
time.sleep(5)

while screenshotCount < int(pages):
    screenshot([x, y, width, height])
    pyautogui.press("right")
    screenshotCount += 1
    time.sleep(1)

print("Do you want to create a PDF? (y/n)")
pdf = input().lower()

if pdf == "j" or pdf == "y":
    print("Do you want to use OCR? (y/n)")
    ocr: str = input().lower()
    if ocr == "":
        ocr = "n"
    print(fill)

if pdf == "j" or pdf == "y" and ocr == "n":
    pdf = fpdf.FPDF()
    for i in range(0, screenshotCount):
        pdf.add_page()
        pdf.image(target + "/screenshot" + str(i) + ".png", 0, 0, 210, 297)
    pdf.output(target + "/" + ausgabeName + ".pdf", "F")
    print("PDF created")

    # Löschen der Screenshots auf Windows
    if os.name == "nt":
        for i in range(0, screenshotCount):
            os.remove(target + "/screenshot" + str(i) + ".png")

    # Löschen der Screenshots auf Linux
    if os.name == "posix":
        for i in range(0, screenshotCount):
            os.system("rm " + target + "/screenshot" + str(i) + ".png")

    print("Screenshots deleted")

if pdf == "y" or pdf == "j" and ocr == "j" or ocr == "y":
    try:
        ocr_funktion(screenshotFolderString, screenshotCount, ausgabeName)
    except:
        print("Make sure that Tesseract is installed")
        print("C:\Program Files\Tesseract-OCR\tesseract.exe")

else:
    print("PDF not created")

print("Program ended")
