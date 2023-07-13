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


a = input("Install OCR packages with? y/n:  ")

if a == "y" or a == "Y":
    print("Standard packages are installed")
    install()
    print("OCR packages are installed")
    ocr()
else:
    install()
    
print("Installation completed")

