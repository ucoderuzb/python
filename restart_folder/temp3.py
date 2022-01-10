from tkinter import*


main = Tk()
main.geometry("400x500")
main.title("photo.exe")
main.configure(bg = 'dark blue')


yuz = Canvas(bg = 'orange', width = 100, height = 90, bd = 2)
yuz.place(x = 146, y = 0)

soch = Canvas(bg = 'black', width = 110, height = 20, bd = 2)
soch.place(x = 146, y = 0)

kuz = Canvas(bg = 'black', width = 15, height = 15)
kuz.place(x = 160, y = 22)

kuz2 = Canvas(bg = 'black', width = 15, height = 15)
kuz2.place(x = 220, y = 22)

burun = Canvas(bg = 'orange', width = 20, height = 20)
burun.place(x = 187.5, y = 40)

ogiz = Canvas(bg = 'red', width = 80, height = 10)
ogiz.place(x = 160, y = 70)

kuylak = Canvas(bg = 'white', width = 130, height = 147, bd = 2)
kuylak.place(x = 150, y = 98)

galyustuk = Canvas(bg = 'red', width = 8, height = 50, bd = 2)
galyustuk.place(x = 192 ,y = 120)

galyustuk3 = Canvas(bg = 'red', width = 10, height = 10, bd = 2)
galyustuk3.place(x = 200 ,y = 110)

galyustuk2 = Canvas(bg = 'red', width = 10, height = 10, bd = 2)
galyustuk2.place(x = 181 ,y = 110)

kiyim = Canvas(bg = 'black', width = 85, height = 150, bd = 2)
kiyim.place(x = 100, y = 95)

kiyim2 = Canvas(bg = 'black', width = 85, height = 150, bd = 2)
kiyim2.place(x = 207, y = 95)

oyoq = Canvas(bg = 'black', width = 70, height = 160, bd = 2)
oyoq.place(x = 160, y = 252 )

kamar = Label(text = 'Dasturchi',bg = 'brown', width = 25, height = 3, bd = 2)
kamar.place(x = 110, y = 200)

entry = Entry(bg = 'white', width = 12, bd = 2, font = 10)
entry.place(x = 280, y = 0, height = 30)

malumot = Button(text = 'Yuqoridagiga\n ismingizini kiriting va\n Enterni bosing!!!',bg = 'white', width = 18, bd = 2)
malumot.place(x = 259, y = 32, height = 50)

def jon():
    kamar.config(text = str("Assalumu alaykum\n") + str(entry.get()) + str("\naka yoki opa men Umidjonman"))

button = Button(text = 'Enter',bg = 'blue', width = 12, bd = 2, font = 10, command = jon)
button.place(x = 260, y = 400, height = 50)

main.mainloop()