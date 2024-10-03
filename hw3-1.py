# Name: Hussein Alsaidi
# Date: 02/27/2023
# Description: This is part 2 of the Input/Output/Process homework.



#Colors
BLUE              = "\033[1;34m"
RESET           = "\033[0;0m"

#Function
def StormEffects(windspeed):
    if windspeed >=157:
        print(BLUE+ "This is a category 5 hurricane", RESET)
        print("Catastrophic damage will occur: A high percentage of framed homes will be destroyed, with total roof failure and wall collapse. Fallen trees and power poles will isolate residential areas. Power outages will last for weeks to possibly months. Most of the area will be uninhabitable for weeks or months.")
    elif windspeed >=130:
        print(BLUE + "This is a category 4 hurricane", RESET)
        print("Catastrophic damage will occur: Well-built framed homes can sustain severe damage with loss of most of the roof structure and/or some exterior walls. Most trees will be snapped or uprooted and power poles downed. Fallen trees and power poles will isolate residential areas. Power outages will last weeks to possibly months. Most of the area will be uninhabitable for weeks or months.")
    elif windspeed >=111:
        print(BLUE + "This is a category 3 hurricane", RESET)
        print("Devastating damage will occur: Well-built framed homes may incur major damage or removal of roof decking and gable ends. Many trees will be snapped or uprooted, blocking numerous roads. Electricity and water will be unavailable for several days to weeks after the storm passes.")
    elif windspeed>= 96:
        print(BLUE + "This is a category 2 hurricane", RESET)
        print("Extremely dangerous winds will cause extensive damage: Well-constructed frame homes could sustain major roof and siding damage. Many shallowly rooted trees will be snapped or uprooted and block numerous roads. Near-total power loss is expected with outages that could last from several days to weeks.")
    elif windspeed>=74:
        print(BLUE + "This is a category 2 hurricane", RESET)
        print("Very dangerous winds will produce some damage: Well-constructed frame homes could have damage to roof, shingles, vinyl siding and gutters. Large branches of trees will snap and shallowly rooted trees may be toppled. Extensive damage to power lines and poles likely will result in power outages that could last a few to several days.")
    else:
        print("This is below the hurricane level wind speeds!")


#Main
windspeed = int(input("Please enter sustained wind speed:"))
StormEffects(windspeed)