import tkinter
from tkinter import Entry

def button_clicked():
    my_label.config(text = input.get(), font=('Arial', 12, 'bold'))
    input.delete(0, 'end')

window = tkinter.Tk()

window.title('My first GUI Program')
window.minsize(400, 300)
window.config(padx = 100, pady = 100)

my_label = tkinter.Label(text='I am a Label', font = ('Arial', 12, 'bold'))
# my_label.pack()
my_label.grid(row=0, column=0)
my_label.config(padx = 50, pady = 50)

my_label.config(text = 'TEST', font=('Arial', 12, 'bold'))

button = tkinter.Button(window, text = 'Hello', font = ('Arial', 12, 'bold'), command = button_clicked)
# button.pack()
button.grid(row=1, column=1)

button2 = tkinter.Button(window, text = 'Hello', font = ('Arial', 12, 'bold'), command = button_clicked)
button2.grid(row=0, column=2)

input = Entry(width=10)
input.get()
input.grid(row=2, column=3)
# input.pack()

window.mainloop()