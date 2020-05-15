# python random module
import random

# number of attempts
attempts = 0

# choose a random number
number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")

# while the player's guesses are less then 6
while attempts < 6:
    guess = input("Take a guess: ")
    guess = int(guess)

    attempts += 1

    # if the players guess is too low
    if guess < number:
        print("Higher")
    
    # if the players guess is too high
    if guess > number:
        print("Lower")

    # if the player won then stop the loop
    if guess == number:
        break

# if the player won
if guess == number:
    attempts = str(attempts)
    print("Good job! You guessed my number in " + attempts + " guesses!")

# if the player lost 
if guess != number:
    number = str(number)
    print("Nope, The number I was thinking of was " + number)