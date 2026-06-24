# What *args and **kwargs mean
# *args → collects extra positional arguments into a tuple.
# **kwargs → collects extra keyword arguments into a dictionary.

def print_args(a, b, *args, **kwargs):
    print(a,b)
    print(args)
    print(kwargs)


print_args(1,2,3,4,5,c=2, d=4)