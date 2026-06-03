product_data = {
    101: {"name": "Laptop", "price": 1200, "category": "Electronics"},
    102: {"name": "Mouse", "price": 25, "category": "Electronics"},
    103: {"name": "Keyboard", "price": 45, "category": "Electronics"},
    104: {"name": "Coffee Mug", "price": 15, "category": "Home Decor"},
    105: {"name": "Desk Lamp", "price": 35, "category": "Home Decor"},
    106: {"name": "Notebook", "price": 5, "category": "Stationery"}
}

tax = (0.05, "$")

def process_checkout (*item_ids, **discounts):
    tax_rate, currency = tax
    
    cart = []
    unique_categories = set()
    subtotal = 0
    
    # for product in item_ids:
    #     if product in product_data:
    #         product = product_data[product]
    #         cart.append(product)
    #         unique_categories.add(product["category"])
    #         subtotal += product["price"]
    #     else:
    #         print("product it not found")
    
    for p in item_ids:
        if p in product_data:
            p = product_data[p]
            cart.append(p)
            print(cart)
            unique_categories.add(p["category"])
            subtotal += p["price"]
            print(f"Total price {subtotal}")
    applied_discount = 0
    if "SAVE10" in discounts and discounts["SAVE10"] == True:
        applied_discount = subtotal * 0.10
        print("you got a discount on you first order")
        
    
        
        
process_checkout(101,102,101, SAVE10 = True)