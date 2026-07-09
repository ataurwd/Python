"""
Simple definition:
A function calling itself until a stopping condition is met.
"""

def count(n):
    if n == 5:
        return
    
    print(n)
    
    count(n + 1)
    
count(1)
