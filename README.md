
# Screenshot's to PDF

[![jhc github](https://img.shields.io/badge/GitHub-CKnuchel-181717.svg?style=flat&logo=github)](https://github.com/CKnuchel)
[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

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
  pip install -r ./requirements.txt
```

Start the Programm

```bash
  python3 ./main.py
```

