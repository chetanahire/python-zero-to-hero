x = 'global'

def outer():
    x = 'enclosing'

    def inner_global():
        global x
        x = 'modified by global'

    def inner_nonlocal():
        nonlocal x
        x = 'modified by nonlocal'

    print(f"Before inner calls: {x}")  # enclosing

    inner_nonlocal()
    print(f"After nonlocal: {x}")  # modified by nonlocal

    inner_global()
    print(f"After global: {x}")  # modified by nonlocal (unchanged)

outer()
print(f"Global x: {x}")  # modified by global