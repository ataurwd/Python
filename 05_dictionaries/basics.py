# Example 1: Creation and Access
user = {
    "name": "Ataur",
    "age": 23,
    "city": "Dhaka"
}

# Dictionary Methods:
# 1. clear() - Removes all elements from the dictionary
# 2. copy() - Returns a copy of the dictionary
# 3. fromkeys() - Returns a dictionary with the specified keys and value
# 4. get() - Returns the value of the specified key
# 5. items() - Returns a list containing a tuple for each key value pair
# 6. keys() - Returns a list containing the dictionary's keys
# 7. pop() - Removes the element with the specified key
# 8. popitem() - Removes the last inserted key-value pair
# 9. setdefault() - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# 10. update() - Updates the dictionary with the specified key-value pairs
# 11. values() - Returns a list of all the values in the dictionary

print(f"Name: {user['name']}")
print(f"City: {user.get('city', 'Unknown')}")

# Example 2: Adding and Updating
user["profession"] = "Developer"
user["age"] = 24
print(f"Updated user: {user}")

# Assignment 1: Create a dictionary representing a book with keys: title, author, and year.
books = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "year": 1960
}

# Assignment 2: Remove the "city" key from the user dictionary using the del keyword.
del user["city"]
print(user)


# how to write multiplle dictionaries in one line
persons = ({"name": "Alice", "age": 30}, {"name": "Bob", "age": 25})

#to get the first one
first_person_name = persons[0]["name"]
print(f"first person name: {first_person_name} and his age is {persons[0]['age']}")