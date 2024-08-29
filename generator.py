import random
import string
import pyperclip

# Generate random string with letters, digits, and symbols
characters = string.ascii_letters + string.digits + string.punctuation

# Get and randomise string with character length from user input
number_of_characters = int(input("Enter the length of the string: "))
random_string = "".join(random.choice(characters) for _ in range(number_of_characters))

# Check if copy to clipboard is available
if pyperclip.is_available():
    pyperclip.copy(random_string)
    print("Random string copied to clipboard!")

if not pyperclip.is_available():
    print("Copy functionality unavailable!")
    print("Please copy the string manually.")

print("<===============================================>\n\nRandom string is:", random_string)
print("\n<===============================================>")
