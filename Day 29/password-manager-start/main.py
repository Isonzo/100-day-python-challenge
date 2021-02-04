import tkinter as tk
from tkinter import messagebox
import random
import pyperclip as pc

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():


    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]

    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    password_list += [random.choice(symbols) for _ in range(nr_symbols)]


    random.shuffle(password_list)

    gen_password = "".join(password_list)

    password.delete(0, tk.END)
    password.insert(0, gen_password)
    pc.copy(gen_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website.get()
    email = name.get()
    passw = password.get()

    if web == "" or email == "" or passw == "":
        messagebox.showinfo("Fields Empty", "Please don't leave empty fields!")
    else:

        is_ok = messagebox.askokcancel(web, "These are the details entered:\n"
                                             f"Email: {email}\nPassword: {passw}\n"
                                             "Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{web} | {email} | {passw}\n")

        website.delete(0, tk.END)
        password.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image((100,100), image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)

name_label = tk.Label(text="Email/Username:")
name_label.grid(row=2, column=0)

pass_label = tk.Label(text="Password:")
pass_label.grid(row=3, column=0)

# Entries

website = tk.Entry(width=35)
website.grid(row=1, column=1, columnspan=2, sticky="W")
website.focus()

name = tk.Entry(width=35)
name.grid(row=2, column=1, columnspan=2, sticky="W")
name.insert(tk.END, "renato.soverina@gmail.com")

password = tk.Entry(width=21)
password.grid(row=3, column=1, sticky="W")

# Buttons

button_pass = tk.Button(text="Generate Password", command=generate_password)
button_pass.grid(row=3, column=2)

button_add = tk.Button(text="Add", width=36, command=save)
button_add.grid(row=4, column=1, columnspan=2)



window.mainloop()
