import random
import string

# Generate random string with letters, digits, and symbols
characters = string.ascii_letters + string.digits + string.punctuation

# Get and randomise string with character length of 16
random_string = ''.join(random.choice(characters) for _ in range(16))
print("Random string is:", random_string)
