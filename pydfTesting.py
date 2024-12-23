#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 10:27:02 2024

@author: tinpot
"""

from pypdf import PdfReader
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os

number_of_pages = 0
filename = ""

def askFilename():
    global filename
    filename = askopenfilename()
    print(filename)
    return filename

def pagecheck():
    if (filename == ""):
        T.delete(1.0, END)
        T.insert(END, ("File not given"))
    else:
        reader = PdfReader(str(filename))
        number_of_pages = len(reader.pages)
        print("Number of pages : " + str(number_of_pages))
        T.delete(1.0, END)
        T.insert(END, ("Number of pages : " + str(number_of_pages)))

window = Tk()
window.geometry("720x480")
B = Button(window, text ="Pages", command = pagecheck)
B.place(x=50,y=50)

C = Button(window, text ="Filename", command = askFilename)
C.place(x=600,y=50)

T = Text(window, height = 5, width = 52)
Fact = ("Number of pages : ")
T.pack()
T.insert(END, Fact)

window.mainloop()