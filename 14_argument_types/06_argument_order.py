# 6. The Golden Rule: Argument Order

"""
EXPLANATION:
When you use multiple types of arguments together, they MUST follow a 
specific order in the function definition:

1. Standard Positional arguments
2. *args
3. Default (Keyword) arguments
4. **kwargs

HOW IT WORKS:
If you mix this order, Python will throw a 'SyntaxError'. Python needs this 
strict order to correctly 'pack' and 'unpack' the values you send.
"""

def complex_function(required_pos, *args, default_param="Default", **kwargs):
    print(f"Positional: {required_pos}")
    print(f"Args (Tuple): {args}")
    print(f"Default: {default_param}")
    print(f"Kwargs (Dict): {kwargs}")

print("--- Running Complex Function ---")
complex_function("MainValue", 1, 2, 3, default_param="Modified", extra="Info", status="OK")
