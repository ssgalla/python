# python random module
import random

# intro
print("Rock, Paper, Scissors...")

# function for processing random item from rock, paper and scissors
def try_again():
    # random choice (rock, paper or scissors)
    R_P_S = ["Rock", "Paper", "Scissors"]
    computer = random.choice(R_P_S)

    # players choice
    player = input("your choice: ").lower().capitalize()

    # if the program chose rock
    if  computer == "Rock":
        # if the player chose rock
        if player == "Rock":
            print("I chose " + computer + " , you chose " + player + " it's a tie!")
        # if the player chose paper
        elif player == "Paper":
            print("I chose " + computer + " , you chose " + player + " you win!")
        # if the player chose scissors
        elif player == "Scissors":
            print("I chose " + computer + " , you chose " + player + " I win!")
    
    # if the program chose paper
    elif computer == "Paper":
        # if the player chose rock
        if player == "Rock":
            print("I chose " + computer + " , you chose " + player + " I win!")
        # if the player chose paper
        if player == "Paper":
            print("I chose " + computer + " , you chose " + player + " it's a tie!")
        # if the player chose scissors
        if player == "Scissors":
            print("I chose " + computer + " , you chose " + player + " You win!")
    
    # if the program chose scissors
    elif computer == "Scissors":
        # if the player chose rock
        if player == "Rock":
            print("I chose " + computer + " , you chose " + player + " You win!")
        # if the player chose paper
        if player == "Paper":
            print("I chose " + computer + " , you chose " + player + " I win!")
        # if the player chose scissors
        if player == "Scissors":
            print("I chose " + computer + " , you chose " + player + " it's a tie!")

    # if the player wants to play again
    play_again = input("Do you want to play again? Y or N: ").lower().capitalize()
    # if tihe player says Y, go back to the funcion
    if play_again == "Y":
        try_again()
    # if the player says N. say goodbye
    elif play_again == "N":
        print("Goodbye")

# end of function
try_again()