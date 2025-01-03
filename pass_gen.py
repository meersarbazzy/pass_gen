import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Get user inputs
num_letters = int(input("How many letters would you like in your password? "))
num_symbols = int(input("How many symbols would you like? "))
num_numbers = int(input("How many numbers would you like? "))


# Generate the password with random positions
password_hard = (
    [random.choice(letters) for _ in range(num_letters)] +
    [random.choice(symbols) for _ in range(num_symbols)] +
    [random.choice(numbers) for _ in range(num_numbers)]
)
random.shuffle(password_hard)  # Shuffle the characters randomly
password_hard = ''.join(password_hard)  # Join the list into a single string
print(f"Strong password: {password_hard}")
