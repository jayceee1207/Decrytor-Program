# Decrytor-Program
CMPE 103 OBJECT-ORIENTED PROGRAMMING
LAB EXERCISE No 1 – PYTHON STRINGS
PROGRAM 2: Code Decryptor

PROBLEM 2 – DECRYPTION
Write a Python Script that will accept a string as encrypted text and then the program will decrypt it using the following character substitute:

'a' = *, 'e' = & , 'i' = # , 'o' = + 'u' = !

See sample output:

Enter a string to decrypt: th& q!#ck br+wn f+x j!mps +v&r th& l*zy d+g.
The Plain Text:  the quick brown fox jumps over the lazy dog.

PROGRAM PSEUDOCODE:
#Ask the user for their input
#Check each character of the string
#   if character is *, change it to a
#   if character is &, change it to e
#   if character is #, change it to i
#   if character is +, change it to o
#   if character is !, change it to u
#We can use .replace function to change the character in a string directly
#Print the resulting output
#Ask the user if they want to use the program again
#   if yes
#       The Decryptor Program will run again
#The program will end with an exit message

