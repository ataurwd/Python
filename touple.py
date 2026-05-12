color = ("red", "green", "blue")

print(color[0])
# output: red

person = "Ataur Rahman", 18, "developer"
name, age, profession = person
print(f'Name: {name}, Age: {age}, Profession: {profession}')
print(person)

#metrix with touple

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(matrix[2][1])




users = (
    {"name": "Ataur", "age": 20},
    {"name": "John", "age": 17},
    {"name": "Alice", "age": 25}
)

for u in users:
    if u["age"] > 18:
        print(f"Name: {u['name']}, Age: {u['age']}")