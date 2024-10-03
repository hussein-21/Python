# Name: Hussein Alsaidi
# Date: 01/26/2023
# Description: This is part 4 of the Input/Output/Process homework.
import math
# Input
num_eggs = int(input('How many eggs did the restaurant use last month?'))
# Process
cartons1 = num_eggs / 12
cartons2 = math.ceil(12)
cartons3 = -(-num_eggs // 12)
# Output
print('Order',cartons1, 'cartons of eggs next month.')
print('Order',cartons2, 'cartons of eggs next month.')
print('Order',cartons3, 'cartons of eggs next month.')


