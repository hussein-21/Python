# Name: Hussein Alsaidi
# Date: 02/08/2023
# Description: This is part 2 of Homework #2.

def calcTaxes(price):
    SALES_TAX = .06
    # Process
    taxes = SALES_TAX * price
    # Output
    print("Taxes are: "+'${:.2f}'.format(taxes))

# Main1
price = float(input('Please enter the product price:'))
calcTaxes(price)