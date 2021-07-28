"""
Program takes an input and checks to see if the number is in the list
"""

num_list = ["0","2","4","5"] #Create numbers list

while True:
    number = input("Please Guess a Number or type q to quit: ")

    if number == "q":
        break
    elif number in num_list:
        print("You have guessed right!")
    else:
        print("You guessed wrong!")
