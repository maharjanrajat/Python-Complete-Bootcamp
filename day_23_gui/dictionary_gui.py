import tkinter as tk
from tkinter import ttk
import requests

def get_meaning_from_api(word):
    response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    
def button_handler():
    word = word_input.get()
    meaning = get_meaning_from_api(word)

window = tk.Tk()
window.title("Dictionary")
window.geometry('500x200')

word_input = ttk.Entry()
button = ttk.Button(text = "Meaning")
result = ttk.Label(text = " ")


word_input.pack(
    padx=10,
    pady=10,
    side="left",
    fill="x",
    expand=1,
    anchor="nw"
)
button.pack(
    padx = 10,
    pady = 10,
    anchor = "ne"
)
result.pack()



window.mainloop()