# Name: Hussein Alsaidi
# Date: 02/13/2023
# Description: This is part 1 of Exam #1.


#Main
mph=float(input('Enter miles per hour:'))


#Function1
def mph_to_kph():
    kph=mph*1.609
    print(f"{mph:,.1f} mph = {round(kph)} kph")

mph_to_kph()


#Function2
def mph_to_knots():
    knots = mph * 0.868976
    print(f'{mph:.1f} mph = {round(knots)} knots')

mph_to_knots()