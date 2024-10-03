
def calcChange(cents):
    quarters = cents // 25
    # Cents left
    cents = cents - 25 * quarters

    # 10 cents = 1 dimes
    dimes = cents // 10
    # Cents left
    cents = cents - 10 * dimes

    # 5 cents = 1 nickels
    nickels = cents // 5
    # Cents left
    cents = cents - 5 * nickels

    # 1 cent = 1 penny
    pennies = cents

# Print statements
    print('Number of quarters: ', quarters)
    print('Number of dimes: ', dimes)
    print('Number of nickels: ', nickels)
    print('Number of pennies: ', pennies)

# Input the cents
cents = int(input('Enter the number of cents: '))
# Call the function
calcChange(cents)