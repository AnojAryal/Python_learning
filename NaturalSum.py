# ask user for input
n = int(input("Enter a positive integer: "))

# initialize variables
sum = 0
i = 1

# calculate sum of natural numbers up to n
while i <= n:
    sum += i
    i += 1

# print the result
print("The sum of the first", n, "natural numbers is:", sum)
