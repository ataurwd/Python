# 1. Positional Arguments

"""
EXPLANATION:
Positional arguments are the most common type. 
The order (position) in which you pass the values matters. 
The first value goes to the first parameter, the second to the second, and so on.

HOW IT WORKS:
Python matches the values to parameters based strictly on their index in the call.
"""

def introduce(name, age):
    print(f"Hello, my name is {name} and I am {age} years old.")

# Correct order
print("--- Correct Position ---")
introduce("Ataur", 25) 

# Wrong order (The output won't make sense)
print("\n--- Wrong Position ---")
introduce(25, "Ataur") 
