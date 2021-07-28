#Import random module
import random

#This function initialises the hangman game
def hangman(word):
    
    #Define global variables used which belongs to hangman function scope
    global wrong
    global stages
    global remaining_letters
    global board
    global win
    
    #initialise the hangman stages string 
    wrong = 0
    stages = ["",                   #Stage 1
             " _______          ",  #      2
             "|                 ",  #      3
             "|      |          ",  #      4
             "|      0          ",  #      5
             "|    / | \        ",  #      6
             "|     / \         ",  #      7 
             "|                 "   #      8
             ]                      
    #initialise other variables in the game         
    remaining_letters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman!")

"""
The game starts here 

"""
#Create a list of strings
random_list = ["cat", "rabbit", "dog", "hamster"]

#Generate a randomly selected word using the built-in "random" module 
playerOne_word = random.choice(random_list)

#initialise game variables
hangman(playerOne_word)

#start the game
while wrong < len(stages) - 1 :
    
    #Player2 enters letter to guess 
    msg = "Guess a letter: "
    playTwo_letter = input(msg)
    
    #Check if player1 letter is in the guess list  
    if playTwo_letter in remaining_letters:

        letter_index = remaining_letters.index(playTwo_letter)  #Find the index value of letter at that position
        board[letter_index] = playTwo_letter                    #write the correctly guessed letter to the board
        remaining_letters[letter_index] = "$"                   #Replacing remaining letters with a $ sign
    else :
        wrong +=1                                               #If wrong increment the wrong counter 
        
    #Update the values to board 
    print((" ".join(board)))
    error= wrong + 1
    
    #print the hangman stages on the board
    print("\n".join(stages[0:error]))
    
    #Check the board for remaining space
    if "__" not in board:
        print("You win")
        print(" ".join(board))  #print the updated board 
        win = True
        break
if not win:
    print("\n".join(stages[0:wrong]))
    print("You lose! It was {}.".format(playerOne_word))
