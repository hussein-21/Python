# Name: Hussein Alsaidi


def getsidelength1():
    side1= float(input("Please enter length of side #1:"))
    return side1
def getsidelength2():
    side2 = float(input("Please enter length of side #2:"))
    return side2
def calcRecaArea(side1,side2):
    total = side1 * side2
    return total
def Main():
    side1 = getsidelength1()
    side2 = getsidelength2()
    print('the area of the rectangle is: ', calcRecaArea(side1,side2))
Main()






