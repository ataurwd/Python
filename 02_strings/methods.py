text = "  Hello, Python World!  "

# Example 1: Strip, Upper, Lower
print(f"Original: '{text}'")
print(f"Stripped: '{text.strip()}'")
print(f"Uppercase: {text.upper()}")

# Example 2: Replace and Split
new_text = text.replace("Python", "Coding")
words = text.split(",")
print(f"Replaced: {new_text.strip()}")
print(f"Split by comma: {words}")

# Assignment 1: Take the string "python is awesome" and capitalize every word.
# Assignment 2: Count how many times the letter 'o' appears in the string "Hello World".
