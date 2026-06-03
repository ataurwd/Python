# Master Guide: *args and **kwargs in Python

"""
EXPLANATION:
1. *args (Non-Keyword Arguments):
   - Allows a function to accept any number of positional arguments.
   - The 'args' variable becomes a TUPLE inside the function.
   - Use it when you don't know how many inputs the user will provide.

2. **kwargs (Keyword Arguments):
   - Allows a function to accept any number of keyword (named) arguments.
   - The 'kwargs' variable becomes a DICTIONARY inside the function.
   - Use it for optional settings, configurations, or named data.
"""

print("--- Example 1: Basic *args (Summing Numbers) ---")
def sum_numbers(*nums):
    # nums is a tuple: (1, 2, 3)
    total = 0
    for n in nums:
        total += n
    return total

print(f"Sum of 1,2,3: {sum_numbers(1, 2, 3)}")
print(f"Sum of 5,10: {sum_numbers(5, 10)}\n")


print("--- Example 2: Basic **kwargs (User Profile) ---")
def build_profile(name, **info):
    # info is a dictionary: {'age': 25, 'city': 'Dhaka'}
    print(f"User: {name}")
    for key, value in info.items():
        print(f"- {key.capitalize()}: {value}")

build_profile("Ataur", age=25, city="Dhaka", job="Developer")
print()


print("--- Example 3: Combining Both (*args and **kwargs) ---")
def order_food(customer, *items, **extras):
    print(f"Order for: {customer}")
    print(f"Items: {', '.join(items)}")
    if extras:
        print("Special Instructions:")
        for key, val in extras.items():
            print(f"  {key}: {val}")

order_food("Rakib", "Pizza", "Coke", "Fries", delivery="Urgent", discount_code="SAVE20")
print()


print("--- Example 4: Unpacking with * and ** ---")
def multiply(a, b, c):
    return a * b * c

my_list = [2, 3, 4]
my_dict = {'a': 10, 'b': 2, 'c': 5}

# Using * to unpack list into positional arguments
print(f"Unpacked List: {multiply(*my_list)}")
# Using ** to unpack dictionary into keyword arguments
print(f"Unpacked Dict: {multiply(**my_dict)}\n")


print("--- Example 5: Forwarding Arguments (Wrapper) ---")
def logger(func, *args, **kwargs):
    print(f"Executing function: {func.__name__}")
    result = func(*args, **kwargs)
    print(f"Result was: {result}")
    return result

def add(x, y): return x + y
logger(add, 10, 20)
print()


# ==========================================
# ASSIGNMENTS FOR YOU
# ==========================================

"""
ASSIGNMENT 1: 
Create a function called 'concatenate_strings(*args)' that takes any number 
of strings and joins them with a space.
Example: concatenate_strings("Python", "is", "awesome") -> "Python is awesome"

ASSIGNMENT 2:
Create a function 'inventory_manager(category, **items)' that takes a 
category name and any number of items with their quantities.
Example: inventory_manager("Fruits", apples=10, bananas=5, mangoes=20)
Output:
Category: Fruits
- apples: 10
- bananas: 5
- mangoes: 20

ASSIGNMENT 3:
Write a function 'calculate_average(*grades)' that returns the average of 
any number of grades provided. If no grades are provided, return 0.
"""
