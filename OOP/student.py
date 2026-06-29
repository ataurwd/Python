class Student:
    def __init__(self, name, age, dep):
        self.name = name
        self.age = age
        self.dep = dep
        self.course = []
        
    def introduction (self):
        print(
            f"my name is {self.name.title()}."
            f"I'm {self.age} years old ."
            f"i study {self.dep.upper()}"
        )
    def course(self , course):
        self.course.append(course)
        
# student = Student("ataur rahman", 20, "bangla")
# student2 = Student("aysha", 21, "english")
# student.introduction()
# student2.course("python")
# student2.introduction()


# Bank System

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit (self, amount):
        self.balance += amount
    
    def withdraw ( self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("insufficient balance")
    
    def check_balance (self):
        print(self.balance)
        

account = BankAccount("ataur", 1000)

account.deposit(5000)
account.withdraw(3000)
account.check_balance()