# Example 1: Default and Keyword Arguments
def power(base, exponent=2):
    return base ** exponent

print(f"2 squared: {power(2)}")
print(f"2 cubed: {power(2, 3)}")
print(f"Keyword: {power(exponent=4, base=2)}")

# Example 2: *args (Arbitrary arguments)
def sum_all(*nums):
    return sum(nums)

print(f"Sum: {sum_all(1, 2, 3, 4, 5)}")

# Example 3: **kwargs (Arbitrary keyword arguments)
def print_details(**info):
    for key, val in info.items():
        print(f"{key}: {val}")

print_details(name="Ataur", job="Dev", city="Dhaka")

# Assignment 1: Create a function describe_pet that takes pet_name and animal_type (with a default value of 'dog').
# Assignment 2: Write a function that accepts any number of positional arguments and returns their product.
