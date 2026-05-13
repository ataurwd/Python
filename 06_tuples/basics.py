# Example 1: Creation and Indexing
colors = ("red", "green", "blue")
print(f"Second color: {colors[1]}")

# Example 2: Immutability (Tuples cannot be changed)
try:
    colors[0] = "yellow"
except TypeError as e:
    print(f"Error caught: {e} - Tuples are immutable!")

# Example 3: Count and Index
print(f"Index of 'blue': {colors.index('blue')}")

# Assignment 1: Create a tuple with a single element "Python" and verify its type.
# Assignment 2: Concatenate two tuples (1, 2, 3) and (4, 5, 6) into a new tuple.
