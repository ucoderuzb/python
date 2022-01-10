from tkinter import*
main = Tk()
main.title('Daraja.exe')
main.geometry('300x300')
main.configure(bg = 'black', bd = 2)

entry = Entry(bg = 'red', font = 4)
entry.place(x = 105, y = 40, width = 160, height = 40)

entry2 = Entry(bg = 'yellow', font = 4)
entry2.place(x = 105, y = 90, width = 160, height = 40)

button1 = Button(bd = 5, text = 'Son',bg = 'red', font = 4)
button1.place(x = 40, y = 40, width = 60, height = 40)

button2 = Button(bd = 5, text = 'daraja',bg = 'yellow', font = 4)
button2.place(x = 40, y = 90, width = 60, height = 40)

label = Label(bg = 'blue', font = 4)
label.place(x = 105, y = 200, width = 160, height = 40)

def funksiya():
    label.config(text = int(entry.get()) ** int(entry2.get()))
    
enter3 = Button(bd = 5, text = 'Enter', bg = 'green', command = funksiya, font = 15)
enter3.place(x = 105, y = 145, width = 160, height = 40)

button3 = Button(bd = 5, text = 'Javobi',bg = 'blue', font = 4)
button3.place(x = 40, y = 200, width = 60, height = 40)

button4 = Button(bd = 5, text = '>>>',bg = 'green', font = 10)
button4.place(x = 40, y = 145, width = 60, height = 40)


main.mainloop()
