# Author: Andreia Santos
# Scope : week 4 - task 04
# Aim : python program that mocks the collatz algorithm (conjecture (Veritasium))

#1-------------- variable initalization block

user_no=0
trial=0

sequence=[]
posi=0
current=2

#2-------------- Positive number validator block

# Only accepts for the variable user_no some value which is higher than 1 (inclusive)
while user_no <=0:
    trial =trial+1
    user_no=int(input("Please insert a integer positive number " ))

    if trial >=2:
        print("\n\n\nAttention!!! Inserted number should be higher than 0.\nPlease try again\n")


sequence.insert(posi, user_no) # Very beggining of the algorithm. Value inserted by user saved on the list position 0


#3-------------- Collatz algorithm


while current>=2: # cycle executed to guarantee that algorithm end is lower than 2 (exclusively)

# Verify if the sample number is divisible by 2 with remain equal to 0. If this condition is "true" the value is divisible by "/2" and save the result on next position
    if sequence[posi]%2==0:
        current=int(sequence[posi]/2)
        posi=posi+1
        sequence.insert(posi, current)
        #print(sequence)
    else: # if the sample number is not divisible by 2 with remain 0 a new mathematical operation is executed- multiply by 3 and add one value.
        current=int(sequence[posi]*3+1)
        posi=posi+1
        sequence.insert(posi, current)
        #print(sequence)


#4-------------- Output

print("\n\nEND of program\n\nThe positions estimated accordingly to Collatz algoritm are:")


for number in sequence:
  print(number,end=" ")
