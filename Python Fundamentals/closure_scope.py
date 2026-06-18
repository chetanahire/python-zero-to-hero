def make_multiplier(factor):
    """Create a function that multiplies by factor."""
    # factor is captured in the closure

    def multiply(x):
        return x * factor

    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

d = double(5)
t = triple(5)

print(d)  # 10
print(t)  # 15

# Each closure has its own captured 'factor'