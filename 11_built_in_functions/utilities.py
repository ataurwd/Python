names = ["Ataur", "John", "Alice"]
ages = [23, 25, 28]

# Example 1: Enumerate
print("Enumerate example:")
for index, name in enumerate(names):
    print(f"{index}: {name}")

# Example 2: Zip
print("\nZip example:")
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Example 3: Map and Filter
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
doubled = list(map(lambda x: x * 2, numbers))
print(f"\nEvens: {evens}")
print(f"Doubled: {doubled}")

# Assignment 1: Use zip() to combine a list of colors and a list of fruits into a dictionary.
# Assignment 2: Use enumerate() to print a list of items with their index starting from 1 instead of 0.
