# Example 1: Creation and Access
user = {
    "name": "Ataur",
    "age": 23,
    "city": "Dhaka"
}
print(f"Name: {user['name']}")
print(f"City: {user.get('city', 'Unknown')}")

# Example 2: Adding and Updating
user["profession"] = "Developer"
user["age"] = 24
print(f"Updated user: {user}")

# Assignment 1: Create a dictionary representing a book with keys: title, author, and year.
# Assignment 2: Remove the "city" key from the user dictionary using the del keyword.
