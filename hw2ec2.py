# Name: Hussein Alsaidi
# Date: 02/08/2023
# Description: This is part 2 of Homework #2 Extra Credit.


def milesPerGallon():
    milesDriven = int(input('Please enter the miles driven : '))
    gasUsed = int(input('Please enter gallons of gas used: '))
    return milesDriven / gasUsed


if __name__ == '__main__':
    mpg = milesPerGallon()
    print(f'Miles per gallon of the car is: {mpg:.4f}')
