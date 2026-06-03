# Example 1: Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# Example 2: Using range()
print("Counting to 5:")
for i in range(1, 6):
    print(i)

# Example 3: Iterating over a dictionary
user = {"name": "Ataur", "age": 23}
for key, value in user.items():
    print(f"{key}: {value}")

# Assignment 1: Use a for loop to calculate the sum of all numbers in the list [10, 20, 30, 40].
numbers = [10, 20, 30, 40]

total = 0
for num in numbers:
    # total = sum(numbers)
    total += num
print(f"Total: {total}")

# Assignment 2: Print each character of the string "Python" on a new line using a for loop.

for character in "Python":
    print(character)
