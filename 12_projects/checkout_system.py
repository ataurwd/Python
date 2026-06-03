# E-commerce Checkout System
# Demonstrates: tuple, set, list, dict, loop, functions (*args, **kwargs)

# 1. Dictionary: Product Catalog (Product ID -> Name, Price, Category)
CATALOG = {
    101: {"name": "Laptop", "price": 1200, "category": "Electronics"},
    102: {"name": "Mouse", "price": 25, "category": "Electronics"},
    103: {"name": "Keyboard", "price": 45, "category": "Electronics"},
    104: {"name": "Coffee Mug", "price": 15, "category": "Home Decor"},
    105: {"name": "Desk Lamp", "price": 35, "category": "Home Decor"},
    106: {"name": "Notebook", "price": 5, "category": "Stationery"}
}

# 2. Tuple: Constants (Tax Rate, Currency)
# Tuples are good for data that shouldn't change
CONFIG = (0.05, "$") # 5% Tax, USD

def process_checkout(*item_ids, **discounts):
    """
    Function using *args to accept any number of items
    and **kwargs to accept optional discount codes.
    """
    tax_rate, currency = CONFIG # Unpacking tuple
    
    # 3. List: Store items actually found in catalog
    cart = []
    
    # 4. Set: Track unique categories for the summary
    unique_categories = set()
    
    subtotal = 0
    
    # Loop through the arbitrary arguments (*args)
    for pid in item_ids:
        if pid in CATALOG:
            product = CATALOG[pid]
            cart.append(product)
            unique_categories.add(product["category"])
            subtotal += product["price"]
        else:
            print(f"Warning: Product ID {pid} not found in catalog.")

    # Apply discounts using **kwargs
    applied_discount = 0
    if "SAVE10" in discounts and discounts["SAVE10"] == True:
        applied_discount = subtotal * 0.10
        print(f"--- Discount 'SAVE10' applied: -{currency}{applied_discount:.2f} ---")

    # `tax_amount` is calculating the amount of tax to be applied to the subtotal after any discounts
    # have been deducted. It is calculated by multiplying the subtotal minus any applied discount by
    # the tax rate specified in the `CONFIG` tuple.
    tax_amount = (subtotal - applied_discount) * tax_rate
    final_total = (subtotal - applied_discount) + tax_amount

    # Output formatting
    print("\n" + "="*30)
    print("      PURCHASE RECEIPT      ")
    print("="*30)
    
    for item in cart:
        print(f"- {item['name']:<15} {currency}{item['price']:>10.2f}")
    
    print("-" * 30)
    print(f"Subtotal:       {currency}{subtotal:>10.2f}")
    print(f"Discount:      -{currency}{applied_discount:>10.2f}")
    print(f"Tax ({tax_rate*100}%):    {currency}{tax_amount:>10.2f}")
    print("-" * 30)
    print(f"TOTAL:          {currency}{final_total:>10.2f}")
    print("=" * 30)
    
    # Show unique categories using the set
    print(f"Categories: {', '.join(unique_categories)}")
    print("=" * 30 + "\n")

# Main Execution
if __name__ == "__main__":
    # Simulating a shopping cart with product IDs
    # Using *args for items and **kwargs for the discount code
    process_checkout(101, 102, 105, 106, SAVE10=True)
