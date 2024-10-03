# Name: Hussein Alsaidi
# Date: 02/27/2023
# Description: This is part 3 of the  Decisions and Boolean Logic.



#MENU FUNCTION
def displaymenu():
    print("1 - In District")
    print("2 - Out of District Student")
    print("3 - Out of State / International Student")
    student_type =input("Choose one of the above (1-3):")
    return student_type

#CALC FUNCTION
def calctuition():
    if student_type=="1":
        tuition= (credits1*108) + (credits2*200) + ((credits1+credits2) *24) + 50 + 60
    elif student_type=="2":
        tuition= (credits1*188) + (credits2*265) + ((credits1+credits2) *24) + 50 + 60
    elif student_type=="3":
        tuition= (credits1*273) + (credits2*350) + ((credits1+credits2) *24) + 50 + 60

    return tuition


#MAIN
student_type = displaymenu()
credits1=float(input("How many credits of 100 to 200 do you plan to register for? "))
credits2=float(input("How many credits of 300 to 400 do you plan to register for? "))
print("Your tuition cost will be {:.2f}".format(calctuition()))
