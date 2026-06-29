class UpdateCart:
    def __init__(self):
        self.product_data = {
    101: {"name": "Laptop", "price": 1200, "category": "Electronics"},
    102: {"name": "Mouse", "price": 25, "category": "Electronics"},
    103: {"name": "Keyboard", "price": 45, "category": "Electronics"},
    104: {"name": "Coffee Mug", "price": 15, "category": "Home Decor"},
    105: {"name": "Desk Lamp", "price": 35, "category": "Home Decor"},
    106: {"name": "Notebook", "price": 5, "category": "Stationery"}
}
        
    def process_checkout (self, *item_id):
        cart = []
        unique_item = set()
        sub_total = 0
        
        for p in self.product_data:
            product = self.product_data[p]
            cart.append(product)
            unique_item(product["category"])
            sub_total += product["price"]
        else:
            print("print")