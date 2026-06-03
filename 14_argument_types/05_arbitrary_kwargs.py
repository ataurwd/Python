# 5. Arbitrary Keyword Arguments (**kwargs)

"""
EXPLANATION:
Used when you don't know how many KEYWORD (named) arguments will be passed.
It collects them into a DICTIONARY.

HOW IT WORKS:
The double asterisk (**) tells Python: 'Take all the remaining keyword-value 
pairs and pack them into a dictionary named kwargs'.
"""

def save_user_data(user_id, **user_info):
    print(f"\nSaving data for User ID: {user_id}")
    # user_info is a dictionary: {'first_name': 'Ataur', 'city': 'Dhaka'}
    for key, value in user_info.items():
        print(f"{key}: {value}")

save_user_data(101, first_name="Ataur", city="Dhaka", occupation="Developer")
save_user_data(102, email="rakib@example.com", status="Active")
