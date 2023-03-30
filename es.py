# Author: Andreia Santos
# Scope : week 7 - task 07
# Aim : python program take a file input as an argument from command line and count how many "e" there are on the file



# needed function module to receive as an argument the name of the file : sys
import sys
name = sys.argv[1]


# It is assumed that the file is already created and that is on the same directory where this script is running

print("Name  of file that will be upload is: {}".format(name)) # output the name of the file


freqs = {} # dictionary initialization that will save the letters countings

with open(name) as f: # read what is inside 
        for line in f: # go through each line of the line
            for char in line: # go through each character of each line

                freqs.setdefault(char, 0) # when a character is found to be on the file is initialized 

                freqs[char] += 1 # a frequency estimation of the previous found character 


print ("\n\n\The number of times that the character 'e' is found on the file is: {}\n\n\n".format(freqs["e"])) # outputs the freqeuncy of the "e" character

