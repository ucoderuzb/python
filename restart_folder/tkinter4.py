from tkinter import*
a = Tk()
a.geometry('300x300')


b = Entry(text = 'Write your name', font = 20)
b.place(x = 90, y = 1, width = 120, height = 40)


u = Label(text = 'About', bg = 'dark blue', font = 20)
u.place(x = 30, y = 130, width = 250, height = 40)


def javob():
    u.configure(text = 'Bilamiz sening isming ' + str(b.get()))
    
button = Button(text = 'Answer', font = 20,command = javob)
button.place(x = 90, y = 70, width = 120, height = 40)
