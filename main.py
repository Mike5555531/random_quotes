


import tkinter as tk
import requests
from tkinter import PhotoImage

API_URL = "https://zenquotes.io/api/random"

def get_random_quote():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        # ZenQuotes returns a list with one dictionary
        quote = data[0]['q']
        author = data[0]['a']
        return f'"{quote}"\n— {author}'
    except Exception as e:
        return "Error fetching quote: " + str(e)

class QuoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Zen Quote")
        self.quote_label = tk.Label(
            root,
            text="Click 'Get Quote' to fetch a quote",
            wraplength=400,
            justify='center',
            font=("Helvetica", 14)
        )
        self.quote_label.pack(pady=20)
        self.get_quote_button = tk.Button(
            root,
            text="Get Quote",
            command=self.update_quote,
            font=("Helvetica", 12, "bold")
        )
        self.get_quote_button.pack(pady=10)

    def update_quote(self):
        new_quote = get_random_quote()
        self.quote_label.config(text=new_quote)

if __name__ == "__main__":
    root = tk.Tk()
    background_image = tk.PhotoImage(file="background.png")
    background_label = tk.Label(root,image= background_image)
    background_label.place(x=0, y=0,relwidth=1,relheight=1)

    app = QuoteApp(root)

    root.mainloop()


