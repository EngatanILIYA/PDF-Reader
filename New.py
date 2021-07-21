from tkinter import *
# import PyPDF2
import records


root = Tk()
root.title("PDF Reader")
root.geometry("1000x700")
root.configure(bg="#b7b7a4")

bg = PhotoImage(file='images.png')

logoLabel = Label(image=bg, bg="#b7b7a4", width=1000, height=170)
logoLabel.place(x=0, y=130)


# INSTRUCTIONS
instructions = Label(text="Select a PDF file on your computer to extract all its text", bg="#b7b7a4", font="Raleway")
instructions.place(x=300, y=325)


def clearText():
    records.clearTextBox()
    return


def file():
    records.content()
    return


def secondFile():
    records.secondContent()
    return


def openFile():
    browseText.set("Loading...")
    file()

    # Menu
    myMenu = Menu(root)
    root.config(menu=myMenu)

    # Drop Down
    fileMenu = Menu(myMenu, tearoff=False)
    myMenu.add_cascade(label="MENU", menu=fileMenu)
    fileMenu.add_command(label="Open", command=secondFile)
    fileMenu.add_command(label="Clear", command=clearText)
    # fileMenu.add_command(label="Page", command=select)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=root.quit)

    browseText.set("Browse")


# BROWSE BUTTON
browseText = StringVar()
browseBtn = Button(textvariable=browseText, command=openFile, font="Raleway", bg="#efefd0",
                   fg="black", height=2, width=15)
browseBtn.place(x=50, y=200)

browseText.set("Browse")
browseBtn.place(x=425, y=400)


root.mainloop()
