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
blankPdfName = ""
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
        T2.configure(state='normal')
        T2.delete(1.0, END)
        T2.insert(END, ("File not given"))
        T2.configure(state='disabled')
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
    
def popupBlankPDF():
    global TPop
    global top
    top= Toplevel(window)
    top.geometry("360x140")
    top.title("Choose the PDF name")
    
    Label(top, text= "Choose the PDF Name", font=('Mistral 18 bold')).place(x=40,y=10)
    
    TPop = Text(top, height = 1, width = 15)
    text = ("")
    TPop.place(relx=0.5, rely=0.55, anchor='s')
    TPop.insert(END, text)
    
    PopButton = Button(top, text ="Save Blank PDF", command = saveBlankPDF)
    PopButton.place(relx=0.5, rely=0.9, anchor='s')
    
def saveBlankPDF():
    blankPdfName = TPop.get("1.0", 'end-1c')
    T2.configure(state='normal')
    if (blankPdfName == ""):
        T2.configure(state='normal')
        T2.delete(1.0, END)
        T2.insert(END, ("PDF name not given"))
        T2.configure(state='disabled')
        top.destroy()
    else:
        pdfBlank = FPDF()
        pdfBlank.output(blankPdfName)
        top.destroy()

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
        pdf.multi_cell(0, None, str(text) + "\n")
        pdf.output("TEXT.pdf")
        T2.configure(state='normal')
        T2.delete(1.0, END)
        T2.insert(END, ("Text saved as PDF"))
        T2.configure(state='disabled')

window = Tk()
window.geometry("720x480")
window.resizable(False, False)
window.title("PydfManip - PDF Manipulator")
B = Button(window, text ="Pages", command = pagecheck)
B.place(x=50,y=50)

C = Button(window, text ="Filename", command = askFilename)
C.place(x=600,y=50)

D = Button(window, text ="Create Blank", command = popupBlankPDF)
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