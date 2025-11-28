import requests
import tkinter as tk
from tkinter import ttk, messagebox

api_key = "18aee9556e2cfe999af9ce70"
base_url = "https://v6.exchangerate-api.com/v6/"
# url = "https://v6.exchangerate-api.com/v6/18aee9556e2cfe999af9ce70/latest/PHP"

def get_rates(base_currency):
    url = f"{base_url}{api_key}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data["conversion_rates"]

def convert_currency(amount, base_currency, target_currency):
    try:
        # currency rates
        rates = get_rates(base_currency)
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

# GUI
root = tk.Tk() # main window
root.geometry("560x200")
root.resizable(False, False)
root.title("Currency Converter")

from_currency = tk.StringVar()
to_currency = tk.StringVar()
output_label = tk.StringVar()

def target_select(event):
   base_code = from_currency.get()
   chosen_code = to_currency.get()

   try:
        currency_name = codes_dict[base_code]
   except KeyError:
        messagebox.showwarning("Invalid currency", "Please enter a valid currency code.")
        return

   rates = get_rates(base_code)
   rate = rates.get(chosen_code, "")
   from_currency_label.set(f"1 {base_code} - {currency_name} = {rate} {chosen_code}")

# gui functions

def search(event):
    input_curr = event.widget.get().lower()
    data = []
    for code, name in codes_dict.items():
        if input_curr in code.lower() or input_curr in name.lower():
            data.append(code)
    if data:
        event.widget["values"] = data
    else:
        event.widget["values"] = list(codes_dict.keys())

def execute_conversion():
   try:
       amount = float(amount_entry.get())
       base = from_currency.get()
       target = to_currency.get()

       if not target or not base:
           messagebox.showwarning("Invalid currency", "Please select a currency code.")
           return
       elif amount < 0:
           messagebox.showwarning("Invalid amount", "Amount cannot be negative.")
           return

       output = convert_currency(amount, base, target)
       output_label.set(f"{amount} {base} = {output} {target}")

   except ValueError:
       messagebox.showwarning("Invalid amount", "Please enter a valid numeric value.")

# text label
amount_label = tk.Label(root, text = "Amount", font=("Calibri", 14))
amount_label.grid(row=1, column=0, padx=5, pady=5)

result_label = tk.Label(root, textvariable=output_label, font=("Calibri", 20))
result_label.grid(row=4, column=0, columnspan=5, pady=5, sticky="n")

# input box
amount_entry = tk.Entry(root, width=15)
amount_entry.grid(row=1, column=1, padx=0, pady=5)

# chosen currency heading(?)
from_currency_label = tk.StringVar()
from_label = tk.Label(root, textvariable=from_currency_label, font=("Calibri", 15))
from_label.grid(row = 0, column = 0, columnspan = 5, pady = 10, sticky="n")

# dropdown for chosen currency to convert from
codes_dict = get_currency_codes()
choices = list(codes_dict.keys())
currency_dropdown = ttk.Combobox(root, textvariable=from_currency, values=choices, width=15)
currency_dropdown.grid(row=1, column=3, padx=3, pady=3)

currency_dropdown.bind("<KeyRelease>", search)

# drop down for target currency
target_dropdown = ttk.Combobox(root, textvariable=to_currency, values=choices, width=15)
target_dropdown.grid(row=1, column=4, padx=3, pady=3)

target_dropdown.bind("<<ComboboxSelected>>", target_select)
target_dropdown.bind("<KeyRelease>", search)

# conversion button
convert_button = tk.Button(root, text="Convert", command=execute_conversion, width=10)
convert_button.grid(row=3, column=3, padx=5, pady=5)

root.mainloop()