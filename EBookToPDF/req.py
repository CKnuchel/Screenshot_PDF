import subprocess
import sys
import os

def install():
    if os.name == "nt":
        os.system("pip install -U pyautogui")
        os.system("pip install -U fpdf")
        os.system("pip install -U tkinter")

    if os.name == "posix":
        os.system("python3 -m pip install -U pyautogui")
        os.system("python3 -m pip install -U fpdf")
        os.system("python3 -m pip install -U tkinter")
        
def ocr():
    if os.name == "nt":
        os.system("pip install -U pdf2image")
        os.system("pip install -U pytesseract")
        os.system("pip install -U PdfMerger")        
        
        
    if os.name == "posix":
        os.system("python3 -m pip install -U pdf2image")
        os.system("python3 -m pip install -U pytesseract")
        os.system("python3 -m pip install -U PdfMerger")


a = input("OCR-Pakete mit installieren? j/n: ")

if a == "j":
    print("Standartpakete werden installiert")
    install()
    print("OCR-Pakete werden installiert")
    ocr()
else:
    install()
    
print("Installation abgeschlossen")

