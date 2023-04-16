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

username  = input("Please enter your name: ")
print("Hello, ", username)

result = pyg.figlet_format("\nCODE DECRYPTOR", font = "digital")
print (result)
