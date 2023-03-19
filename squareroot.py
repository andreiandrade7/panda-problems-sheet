# Author: Andreia Santos
# Scope : week 6 - task 6
# Aim : python program to estimate the square root of a float number inserted by the user. The aim is to do some research regarding the Newton Method and get familiar with function

no_decimal=0

number= float(input("Insert the desired float number you wish to square root ")) # ask the user the float number
no_decimal= len(str(number).split(".")[1])  # count the number of decimal places of the inserted float number


print ("Decimal no: {} ".format(number))
print ("No of decimal places {} ".format(no_decimal))


