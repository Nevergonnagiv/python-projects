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
