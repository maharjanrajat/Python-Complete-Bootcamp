import tkinter as tk
from tkinter import ttk
import requests

def get_advice_from_api():
    response = requests.get('https://api.adviceslip.com/advice')
    if(response.status_code == 200):
        data = response.json()
        return data['slip']['advice']

def advice_button_handler():
    advice = get_advice_from_api()
    advice_label.configure(text = advice)


window = tk.Tk()
window.title("Random Advice Generator")
window.geometry('500x200')

advice_button = ttk.Button(
    window, 
    text="Get Random Advice",
    command=advice_button_handler,
)

advice_label = ttk.Label(text = "NO Advice!")



advice_button.pack()
advice_label.pack()


window.mainloop()




# https://api.dictionaryapi.dev/api/v2/entries/en/book
