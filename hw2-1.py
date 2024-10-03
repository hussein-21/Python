# Name: Hussein Alsaidi
# Date: 02/08/2023
# Description: This is part 1 of Homework #2.

from datetime import datetime
m2= '1:35 PM'
in_time = datetime.strpdtime(m2, "%I:%M %p")
out_time = datetime.strftime(in_time, "%H:%M")
out_time= input('the current standard time is: ')
m2= print('the current military time is:', in_time)
