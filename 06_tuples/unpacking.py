# Example 1: Basic Unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"x: {x}, y: {y}, z: {z}")

# Example 2: Unpacking with asterisk (*)
fruits = ("apple", "banana", "cherry", "date", "elderberry")
first, *middle, last = fruits
print(f"First: {first}")
print(f"Middle: {middle}")
print(f"Last: {last}")

# Assignment 1: Unpack the tuple (100, 200) into two variables width and height.
# Assignment 2: Use the asterisk * to capture the first two elements of a tuple into one variable and the rest into another.
