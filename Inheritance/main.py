#nheritance মানে Child class, Parent class-এর methods এবং attributes নিজের প্রয়োজনমতো ব্যবহার করতে পারে। প্রয়োজনে Parent থেকেই call হয়, আবার Child চাইলে নিজের implementation দিয়েও Parent-এর method override করতে পারে।

class Food:
    def pizza(self, name):
        self.name = name
        print(f'{self.name} eating pizza')
        
    def burger(self):
        print("burger eating")
        
    def shorma(self):
        print("sharma eating")
        
class ManEating(Food):
    pass

eating_test = ManEating()
eating_test.pizza("Ataur")


