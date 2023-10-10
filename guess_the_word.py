import random

# A random number between 1 and 100
number = random.randint(1, 100)
# The guess count
guess_count = 0

''' As long as the player guesses less than 10 times
    the game rolls and counts the guesses of the player '''

while guess_count < 10:
    guess = int(input("Guess the number 1-100: "))
    guess_count += 1
    # How many guesses does the player have left
    guess_rev = 10 - guess_count
    print() # Some spacin' innit?

    if guess > number:
        print("Too high, try again!")
        print(f"You have {guess_rev} more guesses!")
    elif guess < number:
        print("Too low, try again!")
        print(f"You have {guess_rev} more guesses!")
    else:
        print(f"Congratulations! It was the number {number}")
        break
else:
    print(f"You wasted all of your 10 guesses! the number was {number}")