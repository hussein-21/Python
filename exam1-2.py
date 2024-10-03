# Name: Hussein Alsaidi
# Date: 02/13/2023
# Description: This is part 2 of Exam #1.

def menu():
    print('Main Customer Menu')
    print('-------------')
    print("Check Balance")
    print("Print Bill")
    print("Edit Profile")
    print("Exit")
    choice=str(input('Please enter menu option (1-4):'))
    return choice
#Main
choice=menu()
#Output
print('You chose menu option', choice)
