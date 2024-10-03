# Name: Hussein Alsaidi
# Date: 03/17/2023
# Description: This is part 2 of Exam #2.

def ficoscore(score):
    if score >= 300 and  score <= 579:
        print("Your credit rating is poor")
    elif score >= 580 and  score <= 669:
        print("Your credit rating is fair")
    elif score >= 670 and score <= 739:
        print("Your credit rating is Good")
    elif score >= 740 and score <= 799:
        print("Your credit rating is Very Good")
    elif score >= 800 and score <= 850:
        print("Your credit rating is Excellent")
    else:
        print("Invalid FICO score")

score = int(input("Please enter FICO credit score:"))
ficoscore(score)