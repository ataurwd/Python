# 3. Tuple Unpacking

person = ("ataur", 24)

name , age = person

print(f"Candidate name is {name} and her age is {age}")

# multiple data in tuple

persons = (
    ("ataur rahman", 34),
    ("Abdur Rahim", 56)
)

for n,m in persons:
    print(f"candidata name {n} and age {m}")