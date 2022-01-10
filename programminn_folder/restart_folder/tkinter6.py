from tkinter import*
from math import*
a = Tk()
a.title('sqrt.exe')
a.geometry('400x400')

b = Entry(bg = 'red', bd = 3, font = 4)
b.place(x = 110, y = 40, width = 200, height = 40)

t = Label(bg = 'yellow', bd = 4, font = 4 )
t.place(x = 110, y = 160, width = 200, height = 40)

def funk1():
    t.config(text  = sqrt(int(b.get())))

p = Button(text = 'Enter', bg = 'green', bd = 4, font = 4, command = funk1)
p.place(x = 110, y = 100, width = 200, height = 40)
a.mainloop()