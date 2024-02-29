from tkinter import *

window = Tk()


def calculate():
    miles = int(input_box.get())
    kilometers = round(miles * 1.6, 2)
    km_output_label.config(text=kilometers)


window.title("Miles to Km")
window.config(padx=20, pady=20)

input_box = Entry(width=12)
input_box_label = Label(text="Miles", font=("Arial", 14), padx=5, pady=5)
info_label = Label(text="is equal to", font=("Arial", 14), padx=5, pady=5)
km_output_label = Label(text=f"0", font=("Arial", 14), padx=5, pady=5)
info_km_label = Label(text="Km", font=("Arial", 14), padx=5, pady=5)
button = Button(text='Calculate', padx=5, pady=5, font=("Arial", 12, "bold"), command=calculate)

input_box.grid(column=1, row=0)
input_box_label.grid(column=2, row=0)
info_label.grid(column=0, row=1)
km_output_label.grid(column=1, row=1)
info_km_label.grid(column=2, row=1)
button.grid(column=1, row=2)

window.mainloop()
