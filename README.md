

# PYTHON BEGINNER PROJECTS 

> *Half of what I do is handwriten by me, I hope. - Crci*

Five Python beginner and fun projects for beginners to test their knowledge and made by a beginner for the beginners.

## 1. GUESS THE WORD

```python
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
    
```
## 2. TEMPERATURE MEASURER

```python
# CELSIUS TO FAHRENHEIT:

a = float(input("Celsius: "))
c = (a * 1.8) + 32
print(str(c) + " Fahrenheit")

# FAHRENHEIT TO CELSIUS:

a = float(input("Fahrenheit: "))
c = (a - 32) / 1.8
print(str(c) + " Celsius")

# CELSIUS TO KELVIN:

a = float(input("Celsius: "))
c = a + 273.15
print(str(c) + " Kelvin")

# FAHRENHEIT TO KELVIN:

a = float(input("Fahrenheit: "))
c = (a - 32) / 1.8 + 273.15
print(str(c) + " Kelvin")

# KELVIN TO CELSIUS: 

a = float(input("Kelvin: "))
c = a - 273.15
print(str(c) + " Celsius")

# KELVIN TO FAHRENHEIT

a = float(input("Kelvin: "))
c = (a - 273.15) * 1.8 + 32
print(str(c) + " Fahrenheit")
```

## 3. PYTHAGOREAN THEOREM

```python
import math as m

# PYTHAGOREAN THEOREM ON A RIGHT TRIANGLE / RECTANGLE:
print("RIGHT TRIANGLE / RECTANGLE")

a = float(input("Catheter a: "))            # c = √a²+b²
b = float(input("Catheter b: "))
c = m.sqrt(a**2 + b**2)

print(c)

# PYTHAGOREAN THEOREM ON A SQUARE:
print("SQUARE")

a = float(input("Sides a: "))               # c = √a²+a²
c = a * m.sqrt(2)
print(c)

# PYTHAGOREAN THEOREM ON A TRAPEZOID:   
print("TRAPEZOID")

a = float(input("Base a: "))
b = float(input("Base b: "))                # c = √(a+b)²+h²
h = float(input("Height h: "))

c = m.sqrt((a+b)**2+h**2) 
print(c)

#PYTHAGOREAN THEOREM ON A PARALLELOGRAM:
print("PARALLELOGRAM")

b = float(input("Base b: "))                # c = √b²+h²
h = float(input("Height h: "))
d = m.sqrt(b**2+h**2)
print(d)
```

## 4. RANDOM PASSWORD GENERATOR

```python
import random

# Random keyboard values
numbers = "1234567890"
letters_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters_lowercase = "abcdefghijklmnopqrstuvwxyz"
symbols = ",.-\=-(*&^%$#@!)';[]~`/*-+|@"

def generate_password(len):
    characters = numbers + letters_uppercase + letters_lowercase + symbols
    password = ''.join(random.choice(characters) for i in range(len))
    return password

password = generate_password(12)

print(password)

```

## 5. HANGMAN

```python
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
```






# CREDITS:

I'm highly thanking my 2 index fingers and my brain knowledge for these projects that I made.

I wanted to test my Python knowledge and also help others with these projects.

> *He forgor to credit me 💀 - ChatGPT*




# SMURF CAT

Smurf cat.

> *Smurf Cat - Smurf Cat*