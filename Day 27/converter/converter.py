import tkinter as tk

window = tk.Tk()
window.title("Miles to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

is_equal_to = tk.Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

miles_label = tk.Label(text="Miles")
miles_label.grid(row=0, column=2)

km_label = tk.Label(text="Km")
km_label.grid(row=1, column=2)

miles = tk.Entry(width=5)
miles.insert(0, string="0")
miles.grid(row=0, column=1)

km = tk.Label(text=0)
km.grid(row=1, column=1)


def convert():
    m = float(miles.get())
    km["text"] = str(round(m*1.609, 2))


calculate = tk.Button(text="Calculate", command=convert)
calculate.grid(row=2, column=1)


window.mainloop()
