# Name: Hussein Alsaidi
# Date: 01/26/2023
# Description: This is part 5 of the Input/Output/Process homework.
# Country Population
# Input
country1 = input('Enter the country name: ')
# Process
population1 = int(input('Enter country population: '))
# Input
country2 = input('Enter the country name: ')
# Process
population2 = int(input('Enter country population: '))
# Input
country3 = input('Enter the country name: ')
# Process
population3 = int(input('Enter country population: '))
# Output
print('The population of', country1 + ",",country2 + ", and", country3, 'is: {:,.2f}'.format(population1) + ",", '{:,.2f}'.format(population2) + ", and", '{:,.2f}'.format(population3) + ".")