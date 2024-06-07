import tkinter as tk

window = tk.Tk()
window.title("Hello World")
window.minsize(width= 400, height=200)

my_label = tk.Label(text="My Label")
my_label.pack()

button1 = tk.Button(text="Click Me")
button1.place(x=100, y = 20)


window.mainloop()