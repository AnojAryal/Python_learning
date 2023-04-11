# Using a while loop to get user's name

name = ""  # Initialize an empty string for user's name

# Keep asking for name until a valid name is provided
while not name:
    name = input("Please enter your name: ")
    if not name:
        print("Invalid input. Please enter a valid name.")

print("Hello, " + name + "!")  # Greet the user with their name