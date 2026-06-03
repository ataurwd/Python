class CheckoutSystemMonitor:
    
    def __init__(self):
        self.product_data = {
    101: {"name": "Laptop", "price": 1200, "category": "Electronics"},
    102: {"name": "Mouse", "price": 25, "category": "Electronics"},
    103: {"name": "Keyboard", "price": 45, "category": "Electronics"},
    104: {"name": "Coffee Mug", "price": 15, "category": "Home Decor"},
    105: {"name": "Desk Lamp", "price": 35, "category": "Home Decor"},
    106: {"name": "Notebook", "price": 5, "category": "Stationery"}
}
        self.tax_rate = 0.05
        self.currency = "$"
        
    def process_checkout (self, *item_id, **discount):
        cart = [];
        unique_categories = set()
        sub_total = 0
        
        for p in item_id:
            if p in self.product_data:
                product = self.product_data[p]
                cart.append(product)
                unique_categories.add(product["category"])
                sub_total += product["price"]
            else:
                print("invalid data")
                
        applied_discount = 0
        
        if discount.get("SAVE10"):
            applied_discount = sub_total * 0.10
            print(f"you got a discount {applied_discount} taka on your order")
        
        subtotal_after_tax = sub_total - applied_discount;
        tax_ammount = subtotal_after_tax * self.tax_rate
        total = subtotal_after_tax + tax_ammount
        
        return {
            "cart": cart,
            "category": unique_categories,
            "subtotal": sub_total,
            "discount": applied_discount,
            "tax": tax_ammount,
            "total": total
        }
        
checkout = CheckoutSystemMonitor()

result = checkout.process_checkout(
    101, 102, 103, SAVE10 = True
)

print(result)