import tkinter
main = tkinter.Tk()
main.title("Salom")

rasm = tkinter.Canvas(main, bg = 'aqua', bd = 2, background = 'green', width = 400, height = 400)
rasm.pack()

button =  tkinter.Label(text = 'Mana senga', bg = 'red', bd = 2)
button.place(x = 155, y = 85, width = 120, height = 30)

button2 = tkinter.Entry()
button2.place(x = 155, y = 50, width = 120, height = 30)

def son():
    button.config(text = 'Salom ' + str(button2.get()))

joy = tkinter.Button(text  = 'Javob :', command = son)
joy.place(x = 155, y = 5, width = 120, height = 30)    
        
main.mainloop()
