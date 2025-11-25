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

def get_currency(base_currency):
    url = f"{base_url}{api_key}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()

    return list(data["conversion_rates"].keys())
# GUI
root = tk.Tk() # main window
root.geometry("400x450")
root.resizable(False, False)
root.title("Currency Converter")

label = tk.Label(root, text = "Currency Converter", font=("Calibri", 15))
label.grid(row = 0, column = 0, columnspan = 2, padx=0)

amount_label = tk.Label(root, text = "Amount", font=("Calibri", 14))
amount_label.grid(row=1, column=0, padx=5, pady=5)

amount_entry = tk.Entry(root, width=15)
amount_entry.grid(row=1, column=1, padx=0, pady=5)

choices = get_currency(base_currency="USD")
currency_dropdown = ttk.Combobox(root, values=choices, width=15)
currency_dropdown.grid(row=1, column=3, padx=3, pady=3)
root.mainloop()






