# In Python, functions are treated as first-class objects. 
# This means they can be used just like numbers, strings, or any other variable. 

# We can:
# Assign functions to variables.
# Pass them as arguments to other functions.
# Return them from functions.
# Store them in data structures such as lists or dictionaries

def greeting(name):
    return f'Welcome {name}'

f = greeting  # assigned function as variable

#calling function using variable 
print(f('chetan'))


def fun1(fun, name):
    return fun(name)

# Pass function greeting as arguments to other function (fun1).
print(fun1(greeting, 'Chetan Ahire'))



def fun2(msg):
    
    def fun3():
        return f'Hello {msg}'
    # return from functions
    return fun3

# greeting from innner function
fun4 = fun2("Chetan") 
print(fun4())


def multiplier(factor):

    def multiply(x):
        return x * factor
    
    # return from functions
    return multiply
        
double = multiplier(2)

print(double(5))

# ----Store them in data structures such as lists or dictionaries

def add(a,b):
    return a + b

def substract(a,b):
    return a - b

d = {
    "add" : add,
    "substract" : substract
}

d1 = {
    "add1" : add,
    "substract1" : substract
}

print(d["add"](2,3))
print(d["substract"](2,3))

print(d1["add1"](5,3))
print(d1["substract1"](5,3))

l = [add, substract]

print(l[0](4,4))
print(l[1](4,4))
