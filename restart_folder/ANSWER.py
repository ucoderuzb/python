# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 10:20:46 2022

@author: User
"""

from tkinter import *
main = Tk()
main.geometry("400x400")
main.title("Dars")
main.configure(bg = "dark blue")

entry = Entry(bg = "yellow", foreground = "red", font = 10)
entry.place(x = 130, y = 2, width = 150, height = 30)

entry2 = Entry(bg = "yellow", foreground = "red", font = 10)
entry2.place(x = 130, y = 40, width = 150, height = 30)

label = Label(text = "", bg = "yellow", foreground = "red", font = 10)
label.place(x = 130, y = 120, width = 150, height = 30)

button2 = Button(text = "Name", bg = "blue", foreground = "yellow", font = 10)
button2.place(x = 37, y = 2, width = 90, height = 30)

button2 = Button(text = "Password", bg = "blue", foreground = "yellow", font = 10)
button2.place(x = 37, y = 40, width = 90, height = 30)

button2 = Button(text = "Answer", bg = "blue", foreground = "yellow", font = 10)
button2.place(x = 37, y = 120, width = 90, height = 30)

def funksiya():
    
    if entry.get() == "Umidjon" and entry2.get() == "1212":
        
        label = Label(text = "Succesfull", bg = "yellow", foreground = "red", font = 10)
        label.place(x = 130, y = 120, width = 150, height = 30)
    
    else:
        label = Label(text = "Not succesfull", bg = "yellow", foreground = "red", font = 10)
        label.place(x = 130, y = 120, width = 150, height = 30)

button = Button(text = "Enter", command = funksiya,bg = "blue", foreground = "pink", font = 10)
button.place(x = 130, y = 80, width = 150, height = 30)

main.mainloop()