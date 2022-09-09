from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
CHECK_MARK = "✔"
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

import math

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        logo_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        logo_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        logo_label.config(text="Work", fg=GREEN)

    check_marks.config(text=math.floor(reps / 2) * CHECK_MARK)

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    logo_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    canvas.itemconfig(timer_text, text=f"{0 if count / 60 < 10 else ''}{math.floor(count / 60)}:{0 if count % 60 < 10 else ''}{math.floor(count % 60)}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    elif reps < 8:
        start_timer()
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

logo_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
logo_label.grid(column=1, row=0)

start_button = Button(text="Start", font=(FONT_NAME), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME), command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text="", font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()