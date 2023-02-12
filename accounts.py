# Author: Andreia Santos
# Scope : week 3 - task  03
# Aim : Write a python program that outputs the account number with only the last 4 digits showing (and the first digits replaced with Xs). The program is ready to receive a variable number of digits as bank account number.

#------------------------------------------------------------------------------
# 1 . variable initialization
#------------------------------------------------------------------------------

new_account=[] 
show=4 # number of shown numbers



#------------------------------------------------------------------------------
# 2 . bank account insertion
#------------------------------------------------------------------------------

#select the intended method using the comment operator

#method 2 - user insert the bank digits and all digits are  non visible while inserting them. Necessary to install the python lybrary "pip install pwinput" on the terminal and consequently import it to the script
import pwinput
account = pwinput.pwinput("\n\n\nPlease insert your account no\n",mask='*')


#method 1 - user insert the bank digits and all digits are visible while inserting them
#account=input("\n\n\n Please insert your account no\n")



#------------------------------------------------------------------------------
# 3. Operation on the bank account info - respect security rules
#------------------------------------------------------------------------------


hiden=len(account)-show # number of hidden numbers of the account, replaced by "X"


# cycle that upload all individual bank account digits and save them into a new list ("new_account") accordingly to the security rules
for x in range(0,len(account)):

    if hiden>0:
         new_account.insert(x, "X")
    else:
        new_account.insert(x,account[x])

    hiden=hiden-1;




#------------------------------------------------------------------------------
# 4. Output
#------------------------------------------------------------------------------


new_account="".join(new_account) # join the list digits into a presentable string

print(f"\n\n\nFor security reasons only the last 4 numbers of your account are shown. This is your account number:\n{new_account}\n")

