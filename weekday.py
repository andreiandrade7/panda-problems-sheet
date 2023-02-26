# Author: Andreia Santos
# Scope : week 5 - task 05
# Aim : python program that indicates the user if the current day is "weekday" or "weekend"

#------------------------------------------------------------------------------
# 1 . Find the current date
#------------------------------------------------------------------------------

import datetime # need library to access the date in an automatic way

current_date = datetime.datetime.now() # Gives the current date
current_day=current_date.strftime("%A") # Gives the current weekday (Monday, Tuesdsay, Wednesday, ...)



#------------------------------------------------------------------------------
# 2. Output
#------------------------------------------------------------------------------

# based on the current weekday gives a information to the user

if current_day=="Sunday" or current_day=="Saturday":
    print(f"\n\nIt is the weekend, double YAY!\nIs {current_day} today :)\n\n")

else:
    print(f"\n\nYes, unfortunately today is a weekday.\nIs {current_day} today :(\n\n")
