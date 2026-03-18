# 1. Square of a number with default argument
def square(num=2):
    return num ** 2

# 2. Greeting message with default argument
def greet(name="User"):
    return f"Hello, {name}!"

# 3. Addition of 2 numbers, where 'a' is default and 'b' is given
def add(a=5, b=None):
    if b is None:
        raise ValueError("Please provide value for b")
    return a + b

# Example usages
print("Square (default):", square())
print("Square (of 4):", square(4))

print(greet())
print(greet("Alice"))

print("Addition (default a=5, b=10):", add(b=10))
print("Addition (a=3, b=7):", add(3, 7))