import requests
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from datetime import datetime

api_key = "8f96db84de0dd0181fdb9db6776bfb33"
base_url = "http://api.exchangeratesapi.io/v1/"
# url = "https://v6.exchangerate-api.com/v6/18aee9556e2cfe999af9ce70/latest/PHP"

# API conversion
def convert_currency(amount, base_currency, target_currency):
    try:
        url = f"{base_url}latest?access_key={api_key}"
        response = requests.get(url)
        data = response.json()

        # currency rates
        rates = data["rates"]
        source_rate = rates[base_currency]
        target_rate = rates[target_currency]

        # convert from base to target
        php_amount = amount / source_rate
        target_amount = php_amount * target_rate

        return round(target_amount, 2) # 2 decimal places

    except KeyError:
        return -1







