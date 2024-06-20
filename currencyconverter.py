
def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        raise ValueError("Invalid currency")
    if from_currency == to_currency:
        return amount
    amount_in_usd = amount / exchange_rates[from_currency]
    converted_amount = amount_in_usd * exchange_rates[to_currency]   
    return converted_amount
exchange_rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'GBP': 0.75,
    'INR': 73.5,
    'JPY': 110.0
}
amount = float(input("Yokesh, enter the amount: "))
from_currency = input("Yokesh, enter the currency to convert from (e.g., USD, EUR, GBP, INR, JPY): ").upper()
to_currency = input("Yokesh, enter the currency to convert to (e.g., USD, EUR, GBP, INR, JPY): ").upper()
try:
    converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}, Yokesh!")
except ValueError as e:
    print(e)
