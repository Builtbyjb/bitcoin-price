import requests
import sys


# Checks if the command-line argument is valid
if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
    bitcoin = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")


# Gets the bitcoin price data from the coindesk api
try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    r.json()
except requests.RequestException:
    sys.exit
else:
    # Gets the current bitcoin rate in USD as a floating point number
   rate = r.json()["bpi"]["USD"]["rate_float"]


# Calculates and print the amount
amount = rate * bitcoin
print(f"${amount:,.4f}")





