# Author: Andreia Santos
# Scope : week 2 - task 02
# Aim : python program to estimate the sum of two amount inserted by the user . Both amount should be inserted in cents


print("\n\n\nThe current code intends to add two money amounts inserted by the user/n Both amounts must be inserted on cents\n\n\n")


amount1= int(input ("Enter the first amount in cent: "))
amount2= int(input ("Enter the second amount in cent: "))

sum=amount1+amount2

euro= sum/100



print (f"\nThe sum of {amount1} cents  with {amount2} cents is equal to:\n€ {euro}")
