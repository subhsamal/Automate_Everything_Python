import time
from random import shuffle, choice, randint
from tkinter import *
from tkinter import messagebox
import pyperclip

######## ------------------  TO DO ---------------------- #########


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '+', '~', '`']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    final_password_list = password_letters + password_numbers + password_symbols
    shuffle(final_password_list)

    final_password = "".join(final_password_list)
    password_entry.insert(0, final_password)
    pyperclip.copy(final_password)
    messagebox.showinfo(title='COPIED', message="Your password has been generated and copied to clipboard")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def store_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="ERROR", message="make sure no field is empty")
    else:
        is_true = messagebox.askokcancel(title=website, message=f"the details entered: \nEmail: {email} \n"
                                                                f"Password: {password} \nIs it okay to save?")
        if is_true:
            with open("pass.txt", "a") as pass_file:
                pass_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                email_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pass Vault")
window.config(padx=30, pady=30)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
# canvas.pack()
canvas.grid(row=0, column=1)

# create labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=36)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1, columnspan=1)

# Buttons:
generate_password_button = Button(text="Generate Password", width=12, command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=35, command=store_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
