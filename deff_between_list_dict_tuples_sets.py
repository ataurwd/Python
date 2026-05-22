# 1. List → Ordered + Mutable Collection
# multiple item রাখতে হবে
# order important
# data change/add/remove হবে

users = ["Rahim", "Karim", "Jamal"]
users.append("Sakib")
users.remove("Karim")


# 2. Tuple → Ordered + Immutable
# যখন data change হওয়া উচিত না তখন tuple.

colors = ("red", "green", "blue")
location = (23.8103, 90.4125)
user = (1, "Ataur", "admin")


# 3. Set → Unique Values
# যখন duplicate লাগবে না তখন set.
tags = {"python", "django", "react"}
numbers = [1, 2, 2, 3, 4, 4]

unique = set(numbers)

print(unique)
# {1, 2, 3, 4}




# 4. Dict → Key-Value Data
# সবচেয়ে বেশি use হওয়া structure।
# key দিয়ে value access করতে হবে
# structured object-like data লাগবে

user = {
    "name": "Ataur",
    "age": 22,
    "role": "admin"
}