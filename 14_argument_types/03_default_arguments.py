# 3. Default Arguments

"""
EXPLANATION:
You can provide a default value for a parameter in the function definition.
If the user doesn't provide a value for that argument, the default is used.

HOW IT WORKS:
Python checks if a value was passed for the parameter. If not, it assigns 
 the pre-defined default value to it.
"""

def greet(name, message="Welcome!"):
    print(f"Hello {name}, {message}")

print("--- With provided message ---")
greet("Ataur", "Good Morning!")

print("\n--- Without provided message (Uses Default) ---")
greet("Rakib") 
