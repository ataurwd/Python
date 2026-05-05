name = "ataur rahman"
age = [23, 25, 28]

result = f"My name is {name.title()} and my Age is {age[0]}"
print(result)

#list oparations

numbers = [1, 2, 3, 4, 5]

numbers.extend([6, 7, 8])

numbers.append(9)

numbers.pop(0)

#to search an element in a list
# age_list = [23, 25, 28, 30, 35]
# if 31 in age_list:
#     print("True")
# else:
#     print("Data not matched")

# age_list.sort()
# print(age_list)

# for loop in python

users = [{"name": "ataur rahman", "age": 23, "city": "Dhaka"},
        {"name": "korim khan", "age": 45, "city": "rangpur"}]

for n in users:
    print(f"Name: {n['name'].title()}, and his age is {n['age']} also his home town is {n['city'].title()}\n");


prices = [100, 200, 300, 400, 500]
total = 0

for p in prices:
    total += p

print(f"Total prices is: {total}")