# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 17:37:11 2022

@author: User
"""

from tkinter import*
roof = Tk()
roof.title("Kalkulyator.exe")
roof.geometry("350x400")

#front-end

border = Canvas(bg = "white", highlightbackground = "black", border = -0.5)
border.place(x = 0, y = 0, width = 20, height = 400)

border = Canvas(bg = "white", highlightbackground = "black", border = -0.5)
border.place(x = 20, y = 380, width = 310, height = 20)

border = Canvas(bg = "white", highlightbackground = "black", border = -0.5)
border.place(x = 330, y = 0, width = 20, height = 400)

border = Canvas(bg = "white", highlightbackground = "black", border = -0.5)
border.place(x = 20, y = 0, width = 310, height = 20)

# life

entry = Entry(bg = "white", foreground = "black", font = 343212)
entry.place(x = 25, y = 25, width = 300, height = 50)

button1 = Button(border = 5,text = "1", bg = 'white', font = 12312312)
button1.place(x = 20, y = 100, height = 50, width = 50)

def funk():
    
button1 = Button(border = 5,text = "1", bg = 'white', font = 12312312, command = funk)
button1.place(x = 20, y = 100, height = 50, width = 50)

roof.mainloop()