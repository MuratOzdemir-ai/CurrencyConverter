import requests


def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rates = data.get("rates", {})
        if target_currency in rates:
            return rates[target_currency]
        else:
            print(f"Currency '{target_currency}' not found.")
            return None
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None


def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        converted_amount = amount * rate
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
    else:
        print("Conversion failed.")


if __name__ == "__main__":
    base_currency = input("Enter the base currency (e.g., USD): ").upper()
    target_currency = input("Enter the target currency (e.g., EUR): ").upper()
    amount = float(input("Enter the amount to convert: "))

    convert_currency(amount, base_currency, target_currency)