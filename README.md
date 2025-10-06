# FINE3300-2025-A1

This repository contains Jonathan Hargitai's solutions for FINE3300 (Fall 2025) Assignment 1.

Includes:

Part 1 - Mortgage Payments:

Implemented a `MortgagePayment` class.
   Prompts the user for:
    -Principal amount
    -Quoted annual interest rate (percent)
    -Amortization period (years)
  
  Calculates mortgage payments under different schedules:
    -Monthly
    -Semi-monthly
    -Bi-weekly
    -Weekly
    -Rapid Bi-weekly
    -Rapid Weekly

  Outputs formatted payments rounded to two decimals.
  
  Uses the semi-annual compounding convention used in Canadian fixed-rate mortgages.
  
  Converts the quoted interest rate to an effective annual rate (EAR) and determines the periodic rate for each schedule.
  
  Each payment is calculated using the present-value-of-annuity formula, while rapid payments are based on the monthly value (half for bi-weekly,        quarter for weekly).

Part 2 - Exchange Rate Conversion:
  
  Implemented an 'ExchangeRates' class.
    Prompts the user for:
    -amount
    -Currency to convert from (USD or CAD)

  Outputs automatically the currency to convert to (USD or CAD)
  
  Displays results formatted as currency ($100,000.00 USD = $136,980.00 CAD).
  
  Uses real Bank of Canada data for accuracy.
  
  Formats all outputs with commas and two decimal places.

Example Outputs:
      
  Mortgage Example:
  Input:
    Principal: $500,000
    Quoted Rate: 5.5%
    Amortization: 25 years
    
  Output:
    Monthly Payment: $610.39
    Semi-monthly Payment: $304.85
    Bi-weekly Payment: $281.38
    Weekly Payment: $140.61
    Rapid Bi-weekly Payment: $305.20
    Rapid Weekly Payment: $152.60

  Exchange Example:
  Input:
    -$100,000.00 USD
    -$100,000.00 CAD

  Output:
    -$136,980.00 CAD
    -$73,003.36 USD

Summary of Approach:

  -Created two Python classes: MortgagePayment and ExchangeRates.
  
  -Applied object-oriented programming principles with encapsulated attributes and public methods.

  -Used input() for user prompts as required in the assignment.

  -Implemented formulas for periodic mortgage payments and currency conversions.
  
  -Tested outputs for accuracy and ensured consistent formatting.
  
  -Uploaded all project files to this GitHub repository for submission.
