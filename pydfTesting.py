#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 10:27:02 2024

@author: tinpot
"""

from fpdf import FPDF
from pypdf import PdfReader, PdfWriter
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os

number_of_pages = 0
filename = ""
text = ""
errorText = ""

def askFilename():
    global filename
    filename = askopenfilename()
    print(filename)
    return filename

def pagecheck():
    T2.configure(state='normal')
    if (filename == ""):
        T2.delete(1.0, END)
        T2.insert(END, ("File not given"))
    else:
        if (filename):
            try:
                reader = PdfReader(str(filename))
                number_of_pages = len(reader.pages)
                print("Number of pages : " + str(number_of_pages))
                T2.configure(state='normal')
                T2.delete(1.0, END)
                T2.insert(END, ("Number of pages : " + str(number_of_pages)))
                T2.configure(state='disabled')
            except Exception as e:
                T2.configure(state='normal')
                T2.delete(1.0, END)
                T2.insert(END, ("Invalid File, is it a PDF?"))
                T2.configure(state='disabled')

def saveBlankPDF():
    pdf_writer = PdfWriter()
    page = pdf_writer.add_blank_page(width=8.27 * 72, height=11.7 * 72)
    with open('BLANK.pdf', 'wb') as file:
        pdf_writer.write(file)

def savePDF():
    global text
    text = T.get("1.0", 'end-1c')
    print("My text is : ["+text+"]")
    if (text == ""):
        T2.configure(state='normal')
        T2.delete(1.0, END)
        T2.insert(END, ("Empty text, not saved"))
        T2.configure(state='disabled')
    else:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("helvetica", style="B", size=16)
        pdf.cell(40, 10, str(text))
        pdf.output("TEXT.pdf")
        T2.configure(state='normal')
        T2.delete(1.0, END)
        T2.insert(END, ("Text saved as PDF"))
        T2.configure(state='disabled')

window = Tk()
window.geometry("720x480")
window.resizable(False, False)
window.title("Pydf - PDF Manipulator")
B = Button(window, text ="Pages", command = pagecheck)
B.place(x=50,y=50)

C = Button(window, text ="Filename", command = askFilename)
C.place(x=600,y=50)

D = Button(window, text ="Create Blank", command = saveBlankPDF)
D.place(x=25,y=150)

E = Button(window, text ="Save Text", command = savePDF)
E.place(x=600,y=150)

T = Text(window, height = 12, width = 52)
text = ("")
T.place(relx=0.5, rely=0.5, anchor='s')
T.insert(END, text)

T2 = Text(window, height = 2, width = 52)
errorText = ("ERRORS : NONE")
T2.place(relx=0.5, rely=1, anchor='s')
T2.insert(END, errorText)
T2.config(state=DISABLED)

window.mainloop()