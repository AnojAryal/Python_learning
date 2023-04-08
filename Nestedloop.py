# Get the number of rows from the user
num_rows = int(input("Enter the number of rows: "))

# Outer loop for rows
for i in range(num_rows):
    # Inner loop for columns
    for j in range(num_rows):
        # Check if the current cell is in the upper left or lower right diagonal
        if i == j or i + j == num_rows - 1:
            # Print an asterisk for diagonal cells
            print("*", end="")
        else:
            # Print a space for non-diagonal cells
            print(" ", end="")
    # Print a newline character to move to the next row
    print()
