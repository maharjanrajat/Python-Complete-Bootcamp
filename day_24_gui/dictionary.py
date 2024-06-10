import tkinter as tk
from tkinter import ttk
import requests

def search_keyword(keyword):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{keyword}")
    
    if response.status_code == 200:
        data = response.json()
        meanings = data[0]['meanings']
        definition = meanings[0]['definitions'][0]['definition']
        return definition

def search_button_handler():
    keyword = search_input.get()
    value = search_keyword(keyword)
    search_response.insert(tk.END, value)

window = tk.Tk()
window.title("Dictionary App")
window.geometry("500x200")

search_input = ttk.Entry(window, width=60)
search_button = ttk.Button(window, text="Search",
command = search_button_handler)
search_response = tk.Text(window, height=50, width=100)

search_input.grid(row=0, column=0,padx=10, pady=10)
search_button.grid(row=0, column=1, padx=10, pady=10)
search_response.grid(row=1, column=0, padx=10, pady=10)


window.mainloop()