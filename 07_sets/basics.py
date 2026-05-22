# Example 1: Creation and Uniqueness
numbers = {1, 2, 2, 3, 4, 4, 5}
# print(numbers)
# Result = {1, 2, 3, 4, 5}
# print(f"Unique numbers: {numbers}") # Note: Duplicate 2 and 4 are removed

# # Example 2: Adding and Removing
# fruits = {"apple", "banana"}
# fruits.add("cherry")
# fruits.discard("apple")
# print(f"Set after operations: {fruits}")

# Assignment 1: Convert the list [1, 2, 2, 3, 3, 3] into a set to remove duplicates.
# Assignment 2: Use the clear() method to remove all elements from a set.

# print(len(numbers))


# remove duplicate items
emails = [
    "a@gmail.com",
    "b@gmail.com",
    "a@gmail.com",
]

remove_duplicate = set(emails)
# print(remove_duplicate)

# 4. to find common element Find

frontend = {"HTML", "CSS", "JavaScript"}
backend = {"Python", "JavaScript", "SQL"}

common = frontend.intersection(backend)

print(common)


# 5. Blocked Word Filter

blocked_words = {"spam", "fake", "scam"}

comment = "this product is fake"

words = set(comment.split())

if words.intersection(blocked_words):
    print("Blocked comment")
    
    
