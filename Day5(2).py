# Task 1: Define a function named calculate_square that takes a single argument 'n' and returns the square of 'n'.
def calculate_square(n):
    return n * n

# Task 2: In the main program, ask the user to input a positive integer.
n = int(input("Enter a positive integer: "))

# Task 3: Call the calculate_square function with the user-provided number and display the result.
square = calculate_square(n)
print(f"The square of {n} is: {square}")
