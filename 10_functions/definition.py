# Example 1: Basic Function
def greet(name):
    return f"Hello, {name}!"

print(greet("Ataur"))

# Example 2: Multiple return values
def get_user_info():
    name = "Ataur"
    age = 23
    return name, age # Returns a tuple

u_name, u_age = get_user_info()
print(f"User: {u_name}, Age: {u_age}")

# Assignment 1: Define a function calculate_area that takes length and width and returns the area of a rectangle.
# Assignment 2: Create a function that takes a list of numbers and returns both the maximum and minimum values.
