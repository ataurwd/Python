# Example 1: Basic if-elif-else
age = 20

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")

# Example 2: Logical operators with conditionals
has_ticket = True
is_adult = age >= 18

if has_ticket and is_adult:
    print("Welcome to the show!")
else:
    print("Access denied.")

# Assignment 1: Write an if-else statement to check if a number is even or odd.
# Assignment 2: Determine if a year is a leap year (divisible by 4 but not by 100, unless also divisible by 400).
