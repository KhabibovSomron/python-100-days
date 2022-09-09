from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [ random.choice(letters) for char in range(nr_letters)]
    password_symbols = [ random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [ random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)

    password_input.delete(0, END)
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if password.strip() == "" or website.strip() == "":
        error = messagebox.showerror("Oops", "Please don't leave any fields empty!")
    else:    
        is_ok = messagebox.askokcancel(website, f"These are the entered: \nEmail: {username} \nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {username} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=60)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, pady=3)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1, pady=3)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2, pady=3)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, pady=3)

website_input = Entry(width=53)
website_input.grid(column=1, row=1, columnspan=2, pady=3)
website_input.focus()

username_input = Entry(width=53)
username_input.grid(column=1, row=2, columnspan=2, pady=3)
username_input.insert(0, "habibov20@mail.ru")

password_input = Entry(width=34)
password_input.grid(column=1, row=3, pady=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, pady=3)

add_button = Button(text="Add",width=45, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()