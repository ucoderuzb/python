from tkinter import*
from math import*

root = Tk()
root.title('Kalkulyator.exe')
root.geometry('700x180')
root.configure(bd = 5, bg = 'black')

main1 = Entry(font = 20)
main1.place(x = 0, y = 0, width = 350, height = 50)

main2 = Entry(font = 20)
main2.place(x = 350, y = 0, width = 350, height = 50)

main = Label(bg = 'white', font = 5)
main.place(x = 0, y = 60, width = 700, height = 50)

def func1():
    main.config(text = int(main1.get()) + int(main2.get()))
    
plus = Button(text = '+', font = 5, command = func1)
plus.place(x = 0, y = 120, width = 100, height = 50)

def func2():
    main.config(text = int(main1.get()) - int(main2.get()))
    
minus = Button(text = '-', font = 5, command = func2)
minus.place(x = 100, y = 120, width = 100, height = 50)

def func3():
    main.config(text = int(main1.get()) * int(main2.get()))
    
plus2 = Button(text = '*', font = 5, command = func3)
plus2.place(x = 200, y = 120, width = 100, height = 50)

def func4():
    main.config(text = int(main1.get()) / int(main2.get()))
    
minus2 = Button(text = '/', font = 5, command = func4)
minus2.place(x = 300, y = 120, width = 100, height = 50)

def func5():
    main.config(text = int(main1.get()) ** int(main2.get()))
    
SQ = Button(text = '**', font = 5, command = func5)
SQ.place(x = 400, y = 120, width = 100, height = 50)

def func6():
    main.config(text = sqrt(int(main1.get())))
    
SQ1 = Button(text = 'SQRT1', font = 5, command = func6)
SQ1.place(x = 500, y = 120, width = 100, height = 50)

def func7():
    main.config(text = sqrt(int(main2.get())))
    
SQ2 = Button(text = 'SQRT2', font = 5, command = func7)
SQ2.place(x = 600, y = 120, width = 100, height = 50)

main.mainloop()