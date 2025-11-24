import requests

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

        return target_amount

    except KeyError:
        return -1

print(convert_currency(1, "PHP", "USD"))
print(convert_currency(100000, "KRW", "PHP"))








