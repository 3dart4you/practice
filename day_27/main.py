from tkinter import *

def calculate():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f'{round(km,2)}')

window = Tk()
window.title('Miles to Kilometer Converter')
# window.minsize(250, 150)
window.config(padx = 20, pady = 20)

miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)


miles_label = Label(text='Miles')
miles_label.grid(row=0, column=2)
miles_label.config(padx=10, pady=10)

is_equal_label = Label(text='Is equal to')
is_equal_label.grid(row=1, column=0)

kilometer_result_label = Label(text='0')
kilometer_result_label.grid(row=1, column=1)

kilometer_label = Label(text='km')
kilometer_label.grid(row=1, column=2)

calculate_button = Button(text='Calculate', command=calculate)
calculate_button.grid(row=2, column=1)










window.mainloop()