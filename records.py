from tkinter import *
from tkinter.filedialog import askopenfile
import PyPDF2


# Clear Text Box
def clearTextBox():
    textBox = Text(height=40, width=118, padx=15, pady=15)
    textBox.delete(1.0, END)


def index():
    pass


# read pdf file
def content():
    file = askopenfile(mode='rb', title="Choose a File", filetype=[("PDF file", "*.pdf")])
    if file:
        readPdf = PyPDF2.PdfFileReader(file)
        pages = readPdf.getPage(5)
        pageContent = pages.extractText()

        # TEXT BOX
        textBox = Text(height=40, width=118, padx=9, pady=0)
        textBox.insert(1.0, pageContent)
        textBox.tag_configure('center', justify='center')
        textBox.tag_add('center', 1.0, 'end')
        textBox.place(x=10, y=10)
        scrollBar = Scrollbar()
        scrollBar.pack(side=RIGHT, fill=Y)
        myList = Listbox(yscrollcommand=scrollBar.set)
        myList.insert(1, pages)
        # myList.pack(side=LEFT, fill=BOTH)
        scrollBar.config(command=myList.yview)

        Button(text="Next Page", command=index).place(x=910, y=658)
        Button(text="Previous Page", command=index).place(x=10, y=658)


def secondContent():
    file = askopenfile(mode='rb', title="Choose a File", filetype=[("PDF file", "*.pdf")])
    if file:
        readPdf = PyPDF2.PdfFileReader(file)
        pages = readPdf.getPage(5)
        pageContent = pages.extractText()

        # TEXT BOX
        textBox = Text(height=40, width=118, padx=9, pady=0)
        textBox.insert(1.0, pageContent)
        textBox.tag_configure('center', justify='center')
        textBox.tag_add('center', 1.0, 'end')
        textBox.place(x=10, y=10)
