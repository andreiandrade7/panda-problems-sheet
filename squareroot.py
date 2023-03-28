# Author: Andreia Santos
# Scope : week 6 - task 6
# Aim : python program to estimate the square root of a float number inserted by the user. The aim is to do some research regarding the Newton Method and get familiar with function


#------------------------------------------------------------------------------
# 1 . read input number and estimate relevant info (no. decimal places)
#------------------------------------------------------------------------------

no_decimal=0

number= float(input("Insert the desired float number you wish to square root ")) # ask the user the float number
no_decimal= len(str(number).split(".")[1])  # count the number of decimal places of the inserted float number



print ("No of decimal places {} \n\n\n\n".format(no_decimal))




#------------------------------------------------------------------------------
# 2 . function definition-   estimate the square root throught Newton's method
#------------------------------------------------------------------------------

def my_sqrt(number):
    guess = number/2 # first trial for the guessing. Iterate further for approximate the value 

    value= (guess + number/guess)/2 # estimate a new value
    
    while value != guess:
        guess = value # guess upadated with the new estimate value
        value = (guess + number/guess)/2
    return guess

#------------------------------------------------------------------------------
# 3 . function execution and print its original format
#------------------------------------------------------------------------------

root=my_sqrt(number)
print("The estimated square root for the inserted number:{} is {}\n\n\n\n".format(number, root))

#---------------------------------------------------------------------------------------------------------------------
# 4 . trim the estimated sqare root value accordingly to inserted no. of decimal places used on the number insertion
#---------------------------------------------------------------------------------------------------------------------


root_decimal= x = round(root, no_decimal)

print("The estimated square root with {} decimal places is {}\n\n\n\n".format(number,root_decimal))
