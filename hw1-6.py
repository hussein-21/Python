# Name: Hussein Alsaidi
# Date: 01/26/2023
# Description: This is part 6 of the Input/Output/Process homework.
quiz1 = float(input('Enter your score for Quiz #1: \t\t\t'))
quiz2 = float(input('Enter your score for Quiz #2: \t\t\t'))
quiz3 = float(input('Enter your score for Quiz #3: \t\t\t'))
quiz4 = float(input('Enter your score for Quiz #4: \t\t\t'))
hw1 = float(input('Enter your score for Homework #1: \t\t'))
hw2 = float(input('Enter your score for Homework #2: \t\t'))
hw3 = float(input('Enter your score for Homework #3: \t\t'))
hw4 = float(input('Enter your score for Homework #4: \t\t'))
hw5 = float(input('Enter your score for Homework #5: \t\t'))
hw6 = float(input('Enter your score for Homework #6: \t\t'))
grade = (((quiz1 + quiz2 + quiz3 + quiz4)/4) * .4) + (((hw1 + hw2 + hw3 + hw4 + hw5 + hw6)/6) * .6)
print(" " * 40, "-" * 5)
print('Your grade in this class is',"{0:.0f}%".format(grade))