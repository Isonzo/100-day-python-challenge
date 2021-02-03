import tkinter

window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

# Label

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24))
my_label.grid(row=0, column=0)

# Two ways of updating a lable
my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button


def button_click():
    my_label["text"] = input.get()


def button_exit():
    quit()


button = tkinter.Button(text="Click Me", command=button_click)
button.grid(row=1, column=1)

qbutton = tkinter.Button(text="Don't Click Me", command=button_exit)
qbutton.grid(row=0, column=2)
# Entry

input = tkinter.Entry(width=10)
input.grid(row=2, column=3)


window.mainloop()
