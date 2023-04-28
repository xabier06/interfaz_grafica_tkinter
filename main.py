from tkinter import *

def convertir():
    mi = float(input.get())
    km = mi * 1.60934
    label3.config(text=km)

window = Tk()
window.title("Convertidor de millas a km")
window.minsize(width=330, height=200)
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="mi-km.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

input = Entry(width=10, font=("Arial", 14))
input.insert(END, string="0")
input.grid(column=1, row=1)

label1 = Label(text="Millas", font=("Arial", 14))
label1.grid(column=2, row=1)

lable2 = Label(text="Es igual a", font=("Arial", 14))
lable2.grid(column=0, row=2)

label3 = Label(text="0", font=("Arial", 14))
label3.grid(column=1, row=2)

label4 = Label(text="Km", font=("Arial", 14))
label4.grid(column=2, row=2)

button = Button(text="Calcular", font=("Arial", 14), command=convertir)
button.grid(column=1, row=3)

window.mainloop()