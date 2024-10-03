# Name: Hussein Alsaidi
# Date: 02/27/2023
# Description: This is part 4 of the  Decisions and Boolean Logic.


def passcheck(password):
	flag=0
	if len(password) < 10:
		print("Password must include at least 10 characters.")
		flag = 1
	if password.islower() or password.isupper() :
		print("Password must be mixed case.")
		flag=1
	if not any(char.isdigit() for char in password):
		print("Password must include at least one number.")
		flag=1
	if not any(char in SpecialLetter for char in password):
		print("Password must include at least one special character.")
		flag=1
	if flag == 0:
		print("Valid password")
	if flag == 1:
		print("\nInvalid password")

SpecialLetter = ["$", "!", "@", "$", "%", "^", "&", "*", "#"]
password= input("Please enter password: ")
passcheck(password)







