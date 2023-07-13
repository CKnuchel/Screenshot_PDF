
# Screenshot's to PDF

The Programm will take Screenshots from the active Screen.  
It turns the Pages with the Arrow Key.       
It saves the Screenshots in the selected Directory and creates a PDF out of them. Screenshots get removed after the PDF Creation.  
You can pick the OCR (Optical Character Recognition) Option to make a searchable PDF. (Needs Tesseract)


## Run Locally

Download the Files

```bash
 wget https://github.com/CKnuchel/Screenshot_PDF .
```

Download Tesseract and install it 
```bash
https://github.com/UB-Mannheim/tesseract/wiki
```

Go to the project directory

```bash
  cd EBookToPDF
```

Install dependencies

```bash
  python3 ./req.py
```

Start the Programm

```bash
  python3 ./main.py
```

