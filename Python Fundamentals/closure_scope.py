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
# print(double.__closure__)       # Tuple of cell objects
# print(double.__closure__[0].cell_contents)  # 2  factor
# print(double.__closure__[1].cell_contents)  # 5  x