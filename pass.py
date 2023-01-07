import random

letters = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

print("Password Generator")

while True:
    print("_____________________________________")
    MAX_LETTERS = input("How many letters do you want? ")
    MAX_NUMBERS = input("How many numbers do you want? ")
    MAX_SYMBOLS = input("How many symbols do you want? ")
    
    if MAX_LETTERS.isnumeric() and MAX_NUMBERS.isnumeric() and MAX_SYMBOLS.isnumeric():
        password = random.choice(letters)
        
        for _ in range(int(MAX_LETTERS) - 1):
            password = password + random.choice(letters).lower()
            
        for _ in range(int(MAX_NUMBERS)):
            password = password + random.choice(numbers)
            
        for _ in range(int(MAX_SYMBOLS)):
            password = password + random.choice(symbols)
            
        print("Password: " + password)

    else:
        print("Please enter numbers.")
