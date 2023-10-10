import random as r

# The words in the Hangman app from the words.txt file (3606 words)
words = []
with open('words.txt', 'r') as f:
    for line in f.readlines():
        wordle = line.split()
        for word in wordle:  
            if len(word) == 6:
                words.append(word)
# A random word
chose_word = r.choice(words)
chosen_word = chose_word.lower()

# Every time user guesses a letter, it's stored here
guessed_letters = []

# Maximum ammount of guesses and user's guesses
guesses_max = 15
guesses_user = 0

while True:
    # Display for the current state of the word with underscores for unguessed letters
    display_word = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            display_word = display_word + letter + " "
        else:
            display_word += "_ "

    print("Your word: " + display_word)

    # Ask the user to guess a letter or a word
    guess = input("Guess: ").lower()

    # Check if the input is a single letter and if he didn't guess it before
    if len(guess) == 1 and guess.isalpha() and guess not in guessed_letters:
        guessed_letters.append(guess)

        # Check if it was correct or not
        if guess in chosen_word:
            print("Correct!")
        elif guess not in chosen_word:
            print("Incorrect!")
            guesses_user += 1

        # Check if the player took the dub or the L
        if "_" not in display_word:
            print("Congratulations! You won!")
            exit()
        elif guesses_user >= guesses_max:
            print(f"You've ran out of guesses. Sorry! The word was {chosen_word}")
            break
    # If the user guesses the word by typing it        
    elif guess == chosen_word:
        print("Congratulations! You guessed the word!")
        exit()
    else:
        print("You either guesses that letter or that isn't a letter!")
    
    # A friendly reminder to write the actual word after you name all of the letters
    
