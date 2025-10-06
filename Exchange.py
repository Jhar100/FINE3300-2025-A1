# This program converts amounts between CAD and USD
# Goal is to use this library with the Bank of Canada exchange rate data
# Example: 100 USD to CAD, 100 CAD to USD

# Attributes of ExchangeRates: filename, latest_rate
# Assumes CSV file has valid data and last row contains the latest USD/CAD rate

# Public method: convert
#                takes amount, from_currency, to_currency as parameters
#                returns converted value using the latest exchange rate

# Input to program:
#   Amount using input()
#   From currency (USD or CAD) using input()

# Output from program:
#   Converted value displayed as:
#       $100,000 USD = $136,980.00 CAD
#       $100,000 CAD = $73,003.36 USD

import csv

class ExchangeRates:
    # When the class is created, it will automatically read the latest exchange rate
    def __init__(self, filename):
        self.__filename = filename
        self.__latest_rate = self.__read_latest_rate()   # USD/CAD rate from CSV

    def __read_latest_rate(self):
        # Read the CSV file and extract the most recent USD/CAD rate
        with open(self.__filename, newline="") as csvfile:
            reader = list(csv.DictReader(csvfile))  # read as list
            last_row = reader[-1]                   # get the last row
            usd_cad = float(last_row["USD/CAD"])    # extract USD/CAD rate
        return usd_cad

    def convert(self, amount, from_currency, to_currency):
        # Convert amount between USD and CAD

        # If converting USD to CAD, multiply by the exchange rate
        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.__latest_rate
        # If converting CAD to USD, divide by the exchange rate
        elif from_currency == "CAD" and to_currency == "USD":
            return amount / self.__latest_rate
        # If neither of the currency matches, print a message announcing error
        else:
            print("Only USD and CAD conversions are supported")
        
if __name__ == "__main__":
    filename = "BankOfCanadaExchangeRates.csv"

    # Prompting user for input
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the currency to convert from (USD or CAD): ").upper()

    # Decide target currency automatically
    if from_currency == "USD":
        to_currency = "CAD"
    elif from_currency == "CAD":
        to_currency = "USD"
    else:
        print("Only USD or CAD are supported")

    # Creating an instance of the ExchangeRates class
    exchange = ExchangeRates(filename)

    # Performing the conversion using the convert() method
    result = exchange.convert(amount, from_currency, to_currency)

    print(f"${amount:,.2f} {from_currency} = ${result:,.2f} {to_currency}")