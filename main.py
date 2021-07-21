from tkinter.filedialog import askopenfile
from PyPDF2 import PdfFileReader

file = askopenfile(mode='rb', title="Choose a File", filetype=[("PDF file", "*.pdf")])

# Load the pdf to the PdfFileReader object with default settings
with open(file, "rb") as pdf_file:
    pdf_reader = PdfFileReader(pdf_file)
    print(f"The total number of pages in the pdf document is {pdf_reader.numPages}")

    # if file:
    #     readPdf = PyPDF2.PdfFileReader(file)
    #     pages = readPdf.getPage(5)
    #     pageContent = pages.extractText()
    # pdf_reader = PyPDF2.PdfFileReader(pdf_file)
