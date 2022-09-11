
from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
#-------------------------- CREATE CARDS ----------------------#
try:
    data = pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except:    
    data = pandas.read_csv("data/english_words.csv").to_dict(orient="records")

current_card = choice(data)

def correct_click():
    data.remove(current_card)
    pandas.DataFrame(data).to_csv("data/words_to_learn.csv", index=False)
    next_card()

def next_card():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card = choice(data)
    canvas.itemconfig(card_img, image=front_img)
    canvas.itemconfig(card_title, fill="#000000", text="English")
    canvas.itemconfig(card_content, fill="#000000", text=current_card["English"])
    
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_img, image=back_img)
    canvas.itemconfig(card_title, fill="#ffffff", text="Russian")
    canvas.itemconfig(card_content, fill="#ffffff", text=current_card["Russian"])
#-------------------------- UI SETUP --------------------------#

window = Tk()

window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"))
card_content = canvas.create_text(400, 263, text=current_card["English"], font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(text="", image=right_button_img, highlightthickness=0, background=BACKGROUND_COLOR, command=correct_click)
right_button.grid(column=1, row=1)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(text="", image=wrong_button_img, highlightthickness=0, background=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)


window.mainloop()