# Name: Hussein Alsaidi
# Date: 02/08/2023
# Description: This is part 1 of Homework #2.

def DollarChange(cents):
    quarters= cents // 25
    cents = cents - 25 * quarters
    dimes= cents // 10
    cents = cents - 10 * dimes
    nickels= cents // 5
    cents = cents - 5 * nickels
    pennies= cents // 1
    cents = cents - 1 * pennies

    #Print statements
    print('Number of quarters: ', quarters)
    print('Number of dimes: ', dimes)
    print('Number of nickels: ', nickels)
    print('Number of pennies: ', pennies)

# Input the cents
cents = int(input('Enter the number of cents: '))
# Call the function
DollarChange(cents)

