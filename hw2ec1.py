# Name: Hussein Alsaidi
# Date: 02/08/2023
# Description: This is part 1 of Homework #2 Extra Credit.
#---------------------------------------------------------

def convertToAcre(areaInSquareFeet):
    '''
    function to convert area from square feet
    to acre
    '''


    areaInAcre = areaInSquareFeet / 43560


    return areaInAcre

if __name__ == "__main__":

    areaInSquareFeet = int(input('Please enter the area in square feet : '))
    areaInAcre = convertToAcre(areaInSquareFeet)
    print(f'Area in acre is : {areaInAcre:.4f}')

    exit(0)