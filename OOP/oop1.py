class Car:
    def __init__(self, brand):
        self.brand = brand
        

car1 = Car("Toyota")

# print(car1.brand)

class Users:
    def __init__(self, user_name):
        self.user_name = user_name
        
user1 = Users("ataur rahman")
# print(user1.user_name.capitalize().title())


# how to right a method

class User:
    def __init__(self, name):
        self.name = name
        
    def great(self):
        print("Hello", self.name)
        
    def add_prefix(self):
        print("welcome home Master", self.name.title())
        
user = User("ataur rahman")
user.add_prefix()


# to show user data in object using Class function

class User_data:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def user_object(self):
        print(f"User Name {self.name.title()} and user email is {self.email}")
        
user1_data = User_data("ataur rahman", "ataur@gmail.com")
user1_data.user_object()