# Name: Hussein Alsaidi
# Date: 03/17/2023
# Description: This is part 1 of Exam #2.
def elements(elementabb):
    if elementabb == "H" or elementabb == "h":
        print("This element number and name is: 1 – Hydrogen.")
    elif elementabb == "Y" or elementabb == "y":
        print("This element number and name is: 39 – Yttrium.")
    elif elementabb == "B" or elementabb == "b":
        print("This element number and name is: 5 – Boron.")
    elif elementabb == "C" or elementabb == "c":
        print("This element number and name is: 6 – Carbon.")
    elif elementabb == "O" or elementabb == "o":
        print("This element number and name is: 8 – Oxygen.")
    elif elementabb == "F" or elementabb == "f":
        print("This element number and name is: 9 – Fluorine.")
    else:
        print("Invalid element.")

elementabb = input("Please enter your element abbreviation:")

elements(elementabb)