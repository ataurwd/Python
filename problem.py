users = [
    {"name": "ataur rahman", "age": 16, "city": "Dhaka"},
    {"name": "john doe", "age": 18, "city": "NY"},
    {"name": "jane smith", "age": 25, "city": "London"},
]
result = []
for u in users:
    if(u["age"] >= 18):
        name = u["name"].title()
        city = u["city"].title()
        valid_data = f"Valid User {name} and her city {city}"
        result.append(valid_data)

# print(result)


#solved it like pro useing funciton

def get_user_under_18 (users):
    result = []

    for u in users:
        if u["age"] < 20:
            result.append(f"Name: {u['name']} age: {u['age']} \n")
    return result

r = get_user_under_18(users)
print(r)