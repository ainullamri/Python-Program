from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json
import pyperclip as pyperclip

import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    pass_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_pass = [choice(letters) for _ in range(randint(8, 10))]
    symbol_pass = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_pass = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_pass + symbol_pass + numbers_pass

    shuffle(password_list)
    password = "".join(password_list)
    pass_input.insert(0, string= password)
    pyperclip.copy(password)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_name = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            # Reading the data
            data = json.load(data_file)

    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Error", message="No data file found.")

    else:
        if website_name in data:
            email = data[website_name]['email']
            password = data[website_name]['password']
            messagebox.showinfo(title=website_name, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No detail found for {website_name}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website_name = website_input.get()
    email_name = email_input.get()
    password = pass_input.get()
    new_data = {
        website_name: {
            "email": email_name,
            "password": password,
        }
    }

    if len(website_name) == 0 or len(email_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", mode="r") as password_data:
                # Reading old data
                data = json.load(password_data)
                # Updating old data with new data

        except json.decoder.JSONDecodeError:
            with open("data.json", mode="w") as password_data:
                json.dump(new_data, password_data, indent=4)

        else:
            data.update(new_data)
            with open("data.json", mode="w") as password_data:
                # Saving updated data
                json.dump(data, password_data,indent=4)

        finally:
            website_input.delete(0, END)
            pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Creating the main window
main_window = Tk()
main_window.title("Password Manager")
main_window.config(padx=50, pady=50, width=200, height=200, bg="white")


# Input Image
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# LABEL
# #website label
website = Label()
website.config(text="Website:", bg="white", padx=10)
website.grid(row=1, column=0)

# #Email Label
email_label = Label()
email_label.config(text="Email/Username:", bg="white", padx=10)
email_label.grid(row=2, column=0)

# #Password Label
pass_label = Label()
pass_label.config(text="Password:", bg="white", padx=10)
pass_label.grid(row=3, column=0)

# INPUT
website_input = Entry()
website_input.config(width=32, bg="white")
website_input.focus()
website_input.grid(row=1, column=1, sticky="w")


# email input
email_input = Entry()
email_input.config(width=51, bg="white")
email_input.insert(0, string="ainul.amri44@gmail.com")
email_input.grid(row=2, column=1, columnspan=2, sticky="w")

# #password input
pass_input = Entry()
pass_input.config(width=32, bg="white")
pass_input.grid(row=3, column=1, sticky="w")


# #BUTTON
# generate pass button
generate_pass = Button()
generate_pass.config(text="Generate Password", command=generate_password)
generate_pass.grid(row=3, column=2, sticky="w")

# add button
add_button = Button()
add_button.config(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

# Search Button
search_button = Button()
search_button.config(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)
main_window.mainloop()

