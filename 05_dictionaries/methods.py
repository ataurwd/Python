car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Example 1: Keys, Values, and Items
print(f"Keys: {list(car.keys())}")
print(f"Values: {list(car.values())}")
print(f"Items: {list(car.items())}")

# Example 2: Popping and Clearing
model = car.pop("model")
print(f"Removed model: {model}")
print(f"Remaining car: {car}")

# Assignment 1: Use the update() method to add {"color": "red"} to the car dictionary.
# Assignment 2: Check if the key "brand" exists in the car dictionary using the in operator.
