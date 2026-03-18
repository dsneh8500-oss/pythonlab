def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

# Example usage with keyword arguments
result = simple_interest(principal=1000, rate=5, time=2)
print("Simple Interest:", result)