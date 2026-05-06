users = [
    {"id": 1, "name": "ataur rahman", "age": 23, "city": "Dhaka", "salary": 50000, "active": True},
    {"id": 2, "name": "john doe", "age": 17, "city": "NY", "salary": 0, "active": False},
    {"id": 3, "name": "jane smith", "age": 29, "city": "London", "salary": 80000, "active": True},
    {"id": 4, "name": "ali hossain", "age": 35, "city": "Dhaka", "salary": 120000, "active": True},
    {"id": 5, "name": "maria", "age": 21, "city": "London", "salary": 45000, "active": False},
    {"id": 6, "name": "khan", "age": 40, "city": "NY", "salary": 95000, "active": True},
]

class UserData:
    def __init__(self, users):
        self.users = users

    def get_active_user(self):
        result = {}

        for u in self.users:
            if u["age"] > 18:
                country = u["city"].title()
                if country not in result:
                    result[country] = []
                    result[country].append(u["name"].title())
        return result

ua = UserData(users)
print(ua.get_active_user())