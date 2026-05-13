# Example 1: Simple Lambda
square = lambda x: x * x
print(f"Square of 5: {square(5)}")

# Example 2: Lambda with multiple arguments
add = lambda a, b: a + b
print(f"Add 10 + 20: {add(10, 20)}")

# Example 3: Lambda in sorting
points = [(1, 2), (4, 1), (5, -1), (2, 10)]
points.sort(key=lambda x: x[1])
print(f"Sorted by second value: {points}")

# Assignment 1: Write a lambda function that checks if a number is even.
# Assignment 2: Use a lambda function with filter() to extract all numbers greater than 10 from a list.
