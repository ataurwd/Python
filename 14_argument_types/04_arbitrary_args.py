# 4. Arbitrary Arguments (*args)

"""
EXPLANATION:
Used when you don't know exactly how many POSITIONAL arguments will be passed.
It collects multiple values into a single TUPLE.

HOW IT WORKS:
The asterisk (*) tells Python: 'Take all the remaining positional values 
and pack them into a tuple named args'.
"""

def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    # toppings is a tuple: ('mushrooms', 'extra cheese', 'green peppers')
    for topping in toppings:
        print(f"- {topping}")

make_pizza(12, "mushrooms", "green peppers", "extra cheese")
make_pizza(8, "pepperoni")
