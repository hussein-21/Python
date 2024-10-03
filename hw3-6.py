# Name: Hussein Alsaidi
# Date: 02/27/2023
# Description: This is part 6 of the  Decisions and Boolean Logic.

def gameMenu():
    input("\nThis is Game Menu stub")
def leaderBoards():
    input("\nThis is leaderBoards stub")
def options():
    input("\nThis is options stub")
def minecraftstore():
    input("\nThis is minecraft Store stub")
def help():
    input("\nThis is help stub")



#MAIN
while True:
    print("\n   Minecraft Menu")
    print("----------------------")
    print("1. Play Game")
    print("2. Leaderboards")
    print("3. Options")
    print("4. Minecraft Store")
    print("5. Help")
    print("6. Exit")
    menuchoice=input("\n Enter Menu Choice: ")
    if menuchoice=="1":
        gameMenu()
    elif menuchoice=="2":
        leaderBoards()
    elif menuchoice=="3":
        options()
    elif menuchoice=="4":
        minecraftstore()
    elif menuchoice=="5":
        help()
    elif menuchoice== "6":
        print("Goodbye")
        break
    else:
        input("\nInvalid entry.")



