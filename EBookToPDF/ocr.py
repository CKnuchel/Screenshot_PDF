from ast import main
import os
import pytesseract
from pdf2image import convert_from_path
import PyPDF2
import io

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_funktion(screenshotFolder, screenshotCount, ausgabeName):
    #Bilder in PDF umwandeln mit OCR
    print("OCR is being applied, this may take a moment")
    for i in range(0, screenshotCount):
        pdf = pytesseract.image_to_pdf_or_hocr(screenshotFolder + "/screenshot" + str(i) + ".png", extension="pdf")
        with open(screenshotFolder + "/screenshot" + str(i) + ".pdf", "w+b") as f:
            f.write(pdf)
            f.close()
        os.remove(screenshotFolder + "/screenshot" + str(i) + ".png")
        
    #PDFs zusammenfügen
    pdfs = []
    for i in range(0, screenshotCount):
        pdfs.append(screenshotFolder + "/screenshot" + str(i) + ".pdf")
        
    merger = PyPDF2.PdfMerger()
    
    for pdf in pdfs:
        merger.append(pdf)
    
    merger.write(screenshotFolder + "/" + ausgabeName + ".pdf")
    merger.close()
    
    #PDFs löschen
    for i in range(0, screenshotCount):
        os.remove(screenshotFolder + "/screenshot" + str(i) + ".pdf")
    
    print("OCR completed")
