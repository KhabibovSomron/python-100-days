from tkinter import *
from turtle import window_width

FONTS = ("Arial", 12)

window  = Tk()

window.title("Mile to km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

equal_label = Label(text="is equal to", font=FONTS)
equal_label.grid(column=0, row=1)

mile_input = Entry(width=8)
mile_input.grid(column=1, row=0)

km_result_label = Label(text="0", font=FONTS)
km_result_label.grid(column=1, row=1)

def on_button_click():
    miles = int(mile_input.get())
    km_result_label.config(text=f"{miles * 1.609}")


button = Button(text="Calculate", font=FONTS, command=on_button_click)
button.grid(column=1, row=2)

mile_label = Label(text="Miles", font=FONTS)
mile_label.grid(column=2, row=0)

km_label = Label(text="Km", font=FONTS)
km_label.grid(column=2, row=1)

window.mainloop()