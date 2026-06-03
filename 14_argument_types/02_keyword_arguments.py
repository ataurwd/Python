# 2. Keyword Arguments

"""
EXPLANATION:
Keyword arguments allow you to pass values by explicitly naming the parameters.
The order does NOT matter when you use the parameter names.

HOW IT WORKS:
Python looks at the name (key) provided in the call and matches it to the 
parameter name in the function definition.
"""

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

# Even if we change the order, it works perfectly because of the keywords
print("--- Using Keyword Names ---")
describe_pet(pet_name="Harry", animal_type="Hamster")
describe_pet(animal_type="Dog", pet_name="Willie")
