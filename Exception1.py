def divide(x, y):
    try:
        result = x / y
        print("Result: ", result)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except Exception as e:
        print("An error occurred: ", e)

# Test the function with various inputs
divide(10, 5)
divide(10, 0)
divide("a", 2)
