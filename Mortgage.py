# This program calculates mortgage payments under different schedules
# Goal is to use this library across different mortgage products
# Examples: Monthly, Semi-monthly, Bi-weekly, Weekly, Rapid Bi-weekly, Rapid Weekly

# Attributes of MortgagePayment: quoted_rate, amortization_years
# Assumes user input values are valid (principal, interest rate, amortization period)

# Public method: payments
#                takes principal as parameter
#                returns a tuple with 6 payment amounts
#                corresponding to monthly, semi-monthly, bi-weekly, weekly, 
#                rapid bi-weekly, and rapid weekly

# Input to program: 
#   Principal amount using input()
#   Quoted interest rate in percent using input()
#   Amortization period in years using input()

# Output from program:
#   Formatted payment amounts rounded to 2 decimals displayed as:
#       Monthly Payment: $610.39
#       Semi-monthly Payment: $304.85
#       Bi-weekly Payment: $281.38
#       Weekly Payment: $140.61
#       Rapid Bi-weekly Payment: $305.20
#       Rapid Weekly Payment: $152.60

# import math

class MortgagePayment:
    def __init__(self, quoted_rate, amortization_years):
        # Quoted rate is the annual interest rate
        # Amortization is the number of years the loan will be paid off
        self.__quoted_rate = quoted_rate
        self.__amortization_years = amortization_years

    def payments(self, principal):
        # Convert quoted rate to effective annual rate (EAR)
        # In Canada, mortgage rates are quoted as semi-annually compounded
        # So first convert the semi-annual rate to an effective annual rate
        EAR = (1 + self.__quoted_rate / 200) ** 2 - 1

        # MONTHLY PAYMENT
        # Calculate the monthly periodic rate based on EAR
        r_monthly = (1 + EAR) ** (1 / 12) - 1
        # Total number of monthly payments (years * 12 months)
        n_months = self.__amortization_years * 12
        # Apply annuity formula: P = principal * [r / (1 - (1 + r)^-n)]
        monthly = principal * (r_monthly / (1 - (1 + r_monthly) ** -n_months))

        # SEMI-MONTHLY PAYMENT (24 per year)
        # There are 24 semi-monthly payments per year (2 per month)
        r_semi_monthly = (1 + EAR) ** (1 / 24) - 1
        n_semi_monthly = self.__amortization_years * 24
        semi_monthly = principal * (r_semi_monthly / (1 - (1 + r_semi_monthly) ** -n_semi_monthly))

        # BI-WEEKLY PAYMENT (26 per year)
        # There are 26 bi-weekly payments in a year (every two weeks)
        r_bi_weekly = (1 + EAR) ** (1 / 26) - 1
        n_bi_weekly = self.__amortization_years * 26
        bi_weekly = principal * (r_bi_weekly / (1 - (1 + r_bi_weekly) ** -n_bi_weekly))

        # WEEKLY PAYMENT (52 per year)
        # There are 52 weekly payments per year
        r_weekly = (1 + EAR) ** (1 / 52) - 1
        n_weekly = self.__amortization_years * 52
        weekly = principal * (r_weekly / (1 - (1 + r_weekly) ** -n_weekly))

        # RAPID PAYMENTS
        # Rapid payments are based on dividing the monthly payment:
        #   Rapid bi-weekly = half of monthly
        #   Rapid weekly = one-quarter of monthly
        rapid_bi_weekly = monthly / 2
        rapid_weekly = monthly / 4

        # Return all payment values as a tuple in order
        return (monthly, semi_monthly, bi_weekly, weekly, rapid_bi_weekly, rapid_weekly)
    
if __name__ == "__main__":
    # Ask the user to enter mortgage details
    principal = float(input("Enter the mortgage principal amount: "))
    rate = float(input("Enter the quoted interest rate (percent): "))
    years = int(input("Enter the amortization period (years): "))

    # Create an object from the MortgagePayment class using the user input
    mortgage = MortgagePayment(rate, years)

    # Call the payments method to calculate the 6 payment options
    result = mortgage.payments(principal)

    # Display results with 2 decimal places
    # Each print line corresponds to one payment type
    print("Monthly Payment: ${:.2f}".format(result[0]))
    print("Semi-monthly Payment: ${:.2f}".format(result[1]))
    print("Bi-weekly Payment: ${:.2f}".format(result[2]))
    print("Weekly Payment: ${:.2f}".format(result[3]))
    print("Rapid Bi-weekly Payment: ${:.2f}".format(result[4]))
    print("Rapid Weekly Payment: ${:.2f}".format(result[5]))