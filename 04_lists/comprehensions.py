# Example 1: Basic list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Squares: {squares}")

# Example 2: List comprehension with condition
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Assignment 1: Create a list of the first 10 even numbers using list comprehension.
# Assignment 2: Filter a list of strings to only include those with more than 3 characters using list comprehension.
