import requests
import tkinter as tk
from tkinter import ttk, messagebox

api_key = "18aee9556e2cfe999af9ce70"
base_url = "https://v6.exchangerate-api.com/v6/"
# url = "https://v6.exchangerate-api.com/v6/18aee9556e2cfe999af9ce70/latest/PHP"

def convert_currency(amount, base_currency, target_currency):
    try:
        url = f"{base_url}{api_key}/latest/{base_currency}"
        response = requests.get(url)
        data = response.json()

        # currency rates
        rates = data["conversion_rates"]

        # convert from base to target
        target_amount = amount * rates[target_currency]

        return round(target_amount, 2)

    except KeyError:
        return -1


# GUI
root = tk.Tk() # main window
root.geometry("400x450")
root.resizable(False, False)
root.title("Currency Converter")

label = tk.Label(root, text = "Currency Converter")
label.pack()


root.mainloop()






