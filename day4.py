def sum_of_even_numbers(n):
    # Initialize the sum to 0
    total_sum = 0
    
    # Loop through all numbers from 1 to n
    for i in range(2, n + 1, 2):  # Start at 2, step by 2 (even numbers only)
        total_sum += i
        
    return total_sum

# Input from the user
n = int(input("Enter a positive integer: "))

# Check if the input is a positive integer
if n > 0:
    result = sum_of_even_numbers(n)
    print(f"The sum of all even numbers between 1 and {n} is: {result}")
else:
    print("Please enter a positive integer.")
