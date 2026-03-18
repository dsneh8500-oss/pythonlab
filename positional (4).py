import math

# 1. Basic positional argument (sum of two variables)
def sum_two(a, b):
    return a + b

print("Sum:", sum_two(5, 10))


# 2. Student information (Name, roll no, marks)
def student_info(name, roll_no, marks):
    print(f"Name: {name}, Roll No: {roll_no}, Marks: {marks}")

student_info("John", 101, 85)


# 3. Simple interest
def simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si

print("Simple Interest:", simple_interest(1000, 5, 2))


# 4. Area of circle

def ar_circle (r):
    a_circle = 3.14 * r*r
    print("Area of Circle:", a_circle)
ar_circle(1.5)
ar_circle(4)

# 5. Check number if it's positive, negative or zero
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print("Number Check:", check_number(-5))


# 6. Odd or even
def odd_or_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("Odd or Even:", odd_or_even(7))


# 7. Arithmetic operations (addition)
def add(a, b):
    return a + b

print("Addition:", add(15, 25))