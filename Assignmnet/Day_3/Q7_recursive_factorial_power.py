# Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    else:
        return n * factorial(n - 1)   # recursive call

# Recursive function to calculate power (x^n)
def power(x, n):
    if n == 0:   # base case
        return 1
    else:
        return x * power(x, n - 1)   # recursive call

# Example usage
print("Factorial of 5:", factorial(5))   # 120
print("2 raised to power 4:", power(2, 4))  # 16

