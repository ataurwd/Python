"""
===========================================================
POLYMORPHISM IN PYTHON
===========================================================

Definition:
Polymorphism means "One interface, many behaviors."

In this example, the checkout() function doesn't know
whether it receives a Bkash, Nagad, Card, or Rocket object.

It only expects one thing:
    The object must have a pay() method.

Every payment class implements pay() differently.

So...

    checkout(Bkash())  -> Paid with Bkash
    checkout(Nagad())  -> Paid with Nagad
    checkout(Card())   -> Paid with Card
    checkout(Rocket()) -> Paid with Rocket

Notice:
The checkout() function NEVER changes.
Only the object changes.

This is the main idea of Polymorphism.

Real-world example:
Imagine an e-commerce website.

A customer can pay using:
- Bkash
- Nagad
- Card
- Rocket
- PayPal

When the user clicks the "Pay Now" button,
the system simply calls:

    checkout(selected_payment_method)

It doesn't need to know which payment gateway
the customer selected.

As long as every payment class has a pay() method,
checkout() works with all of them.

This makes the code:
✔ Flexible
✔ Reusable
✔ Easy to extend
✔ Easy to maintain

Remember:

    Same function
    Different objects
    Different behaviors

That's Polymorphism.
===========================================================
"""


class Bkash:
    def pay(self):
        print("✅ Paid with Bkash")


class Nagad:
    def pay(self):
        print("✅ Paid with Nagad")


class Card:
    def pay(self):
        print("✅ Paid with Card")


class Rocket:
    def pay(self):
        print("✅ Paid with Rocket")


def checkout(payment_method):
    """
    This function doesn't care what object it receives.
    It only assumes that the object has a pay() method.
    This is where Polymorphism happens.
    """
    payment_method.pay()


# Create objects
bkash = Bkash()
nagad = Nagad()
card = Card()
rocket = Rocket()


# Same function...
# ...Different objects...
# ...Different behaviors.
checkout(bkash)
checkout(nagad)
checkout(card)
checkout(rocket)