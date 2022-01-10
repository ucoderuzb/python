# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 13:58:59 2021

@author: User
"""

import tkinter
a = tkinter.Tk()

a.title("Dasturcha.exe")

b = tkinter.Canvas(a, bg = 'blue', )
b.pack()

g = tkinter.Entry( bg = 'red', bd = 4, font = 5)
g.place(x = 130, y = 50, width = 150, height = 30)

h = tkinter.Label(bg = 'yellow', bd = 4, font = 5)
h.place(x = 110, y = 160, width = 200, height = 30)

def funk1():
    h.config(text = int(g.get()) ** int(2))
    
k = tkinter.Button(text = 'Enter', bg = 'green', bd = 4, command = funk1, font = 4)
k.place(x = 130, y = 100, width = 150, height = 30)

l = tkinter.Label(text = 'Bu dastur xohlagan soningizni kvadrtini chiqaradi.', bg = 'pink', bd = 4, font = 5)
l.place(x = 0, y = 1, width = 380, height = 30)

a.mainloop()
