# L - Local
# E - Enclosing
# G - Global
# B - Built-in
#-----------------------Local-------------------
def calculate():
    x = 10  # Local
    y = 20  # Local
    return x + y

result = calculate()
print(result)

# x is not accessible outside the function

# print(x)  # NameError: name 'x' is not defined

# Local Variables Shadow Outer Scopes

x = 'global'

def show():
    x = 'local' # This creates a new local variable
    print(x)

show() # local
print(x) # global unchanged

#-----------------------Enclosing-------------------

def outer():
    message = 'Hello from outer'  # Enclosing scope variable
    def inner():
        print(message)
    
    inner()

outer()

# multi-level nested function

def level_one():
    a = 'LEVEL ONE'

    def level_two():
        b = 'LEVEL TWO'

        def level_three():
            c = 'LEVEL THREE'
            # Can access a, b, and c
            print(f"a={a}, b={b}, c={c}")

        level_three()

    level_two()

level_one()  # a=one, b=two, c=three


#-----------------------Global-------------------

counter = 0  # global variable

def increment():
    global counter # Declare intention to modify global
    counter += 1

def get_counter():
    return counter

increment()
increment()
print(f'Counter : {get_counter()}')

#-----------------
# The Global Keyword

value = 100

def broken_modify():
    # This creates a LOCAL variable named 'value'
    # It does NOT modify the global 'value'
    value = 200
    print(f"Inside function: {value}")

def working_modify():
    global value  # Now we're talking about the global
    value = 200
    print(f"Inside function: {value}")

broken_modify()
print(f"Global still: {value}")  # 100

working_modify()
print(f"Global now: {value}")  # 200

#-------- BAD: Using global state

total = 0

def add_to_total(x):
    global total
    total += x

add_to_total(5)
add_to_total(3)
print(total)  # 8

# GOOD: Pure function
def add(a, b):
    return a + b

addition = add(0, 5)
addition = add(addition, 3)
print(addition)  # 8

#----------------------Built-in--------------------

# These are all built-ins
print(len([1, 2, 3]))  # len is built-in
print(max(1, 5, 3))    # max is built-in
print(True, False)     # True/False are built-in

# Avoid using these as variable names:
# id, list, dict, set, str, int, float, type, input, print, len, sum, max, min
# open, range, filter, map, sorted, reversed, next, iter

# BAD
id = 42
input = "some value"
type = "string"

# These built-in functions are now broken until you del the variables

# The nonlocal Keyword
# To modify a variable in an enclosing scope (not global), use nonlocal.
def counter():
    count = 0  # Enclosing scope variable

    def increment():
        nonlocal count  # Modify enclosing, not create local
        count += 1
        return count

    return increment

# Create a counter closure
my_counter = counter()
print(my_counter())  # 1
print(my_counter())  # 2
print(my_counter())  # 3