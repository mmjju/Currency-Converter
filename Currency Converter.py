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

def get_currency_codes():
    url = f"{base_url}{api_key}/codes"
    response = requests.get(url)
    data = response.json()

    codes = {code[0]: code[1] for code in data["supported_codes"]}
    return codes

def select(event):
    chosen_code = currency_dropdown.get()
    currency_name = codes_dict.get(chosen_code, "")
    from_currency_label.set(f"1 {chosen_code} - {currency_name}")

def search(event):
    input_curr = event.widget.get().lower()
    data = []
    for code, name in codes_dict.items():
        if input_curr in code.lower() or input_curr in name.lower():
            data.append(code)
    if data:
        currency_dropdown["values"] = data
    else:
        currency_dropdown["values"] = list(codes_dict.keys())

# GUI
root = tk.Tk() # main window
root.geometry("600x250")
root.resizable(False, False)
root.title("Currency Converter")

from_currency = tk.StringVar()
to_currency = tk.StringVar()

# text label
amount_label = tk.Label(root, text = "Amount", font=("Calibri", 14))
amount_label.grid(row=1, column=0, padx=5, pady=5)

# input box
amount_entry = tk.Entry(root, width=15)
amount_entry.grid(row=1, column=1, padx=0, pady=5)

# chosen currency heading(?)
from_currency_label = tk.StringVar()
label = tk.Label(root, textvariable=from_currency_label, font=("Calibri", 15))
label.grid(row = 0, column = 0, columnspan = 3, padx=0)

# dropdown for chosen currency to convert from
codes_dict = get_currency_codes()
choices = list(codes_dict.keys())
currency_dropdown = ttk.Combobox(root, textvariable=from_currency, values=choices, width=15)
currency_dropdown.grid(row=1, column=3, padx=3, pady=3)

currency_dropdown.bind("<<ComboboxSelected>>", select)
currency_dropdown.bind("<KeyRelease>", search)



root.mainloop()






