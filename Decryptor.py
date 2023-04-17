#John Carlo Ablay
#BSCPE 1-5
#Code Encryptor

#PSEUDOCODE
#Ask the user for their input
#Check each character of the string
#   if character is *, change it to a
#   if character is &, change it to e
#   if character is #, change it to i
#   if character is +, change it to o
#   if character is !, change it to u
#Print the resulting output

import pyfiglet as pyg

author_name = ("PROGRAMMED BY: JOHN CARLO ABLAY")
name = author_name.center(100)
print(name)

#Ask the user for their input
username  = input("Please enter your name: ")
print("Hello, ", username)

result = pyg.figlet_format("\nCODE DECRYPTOR", font = "digital")
print (result)

moredata = "yes"
while moredata == "yes":
    #Get the code to decrypt from the user 
    input_string = input("Enter a word: ")
    #Print string
    print("Encrypted String: ", input_string)

    moredata = str(input("Would you like to run the program again? (yes or no): \n"))
