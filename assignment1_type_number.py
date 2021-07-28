"""
:Display message to user and let user enter input
:convert string to integer
:display error message to user if user is unable to convert

"""

import math

num_str = input("Please enter a number: ")

#convert string into an integer
try:
    print(int(num_str))
except:
    print("Please type an integer.")
    
