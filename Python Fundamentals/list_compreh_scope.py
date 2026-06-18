name = 'Suraj'

# The x in comprehension is local to comprehension
result = [name for name in range(3)]
print(result)  # [0, 1, 2]
print(name)       # outer - unchanged!

# In Python 2, this would have changed x to 2