from ast import Delete
from tkinter import *
from tkinter import messagebox
from password_generator import generate_password
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def populate_password():
    password = generate_password()
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_input.get()
    user = email_username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0 or len(user) == 0:
        messagebox.showerror('Error', 'No empty field allowed')
    else:
        is_ok = messagebox.askokcancel(title='website', message=f'These are the details entered: \nEmail: {user} \nPassword: {password} \nIs it ok to save?')

        if is_ok:
            with open("text.txt", "a") as file:
                file.write(f'{website} | {user} | {password} \n')

            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title('Password Manager')
window.config(pady=50, padx=50)


canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)

email_username_label = Label(text="Email/Username")
email_username_label.grid(column=0, row=2)

email_username_input = Entry(width=35)
email_username_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=populate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
