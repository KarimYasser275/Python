from tkinter import *


def calculate():
    miles = input_in_miles.get()
    print(miles)
    if miles != "":
        converted_to_km = int(miles) * 1.609344
        text_3.config(text=str(converted_to_km))
    else:
        text_3.config(text="")


window = Tk(screenName="Mile to KM converter")
window.title("Mile to KM converter")
window.config(height=300, width=500)

input_in_miles = Entry(width=10)
input_in_miles.grid(column=1, row=0)

text_1 = Label(text="Miles")
text_1.grid(column=2, row=0)

text_2 = Label(text="is equal to")
text_2.grid(column=0, row=1)

text_3 = Label(text="")
text_3.grid(column=1, row=1)

text_4 = Label(text="Km")
text_4.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
