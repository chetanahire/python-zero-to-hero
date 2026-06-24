# Inheritance — MRO (Method Resolution Order) with super()
# 
# In Python, the super() function is used to call methods from a parent class in a multiple inheritance scenario. 
# It ensures that methods are executed in the correct order based on the Method Resolution Order (MRO).

# class Parent1:
#     def __init__(self):
#         print("You are parent1")

# class Parent2:
#     def __init__(self):
#         # super().__init__()
#         print("You are parent2")

# class Child(Parent1, Parent2):
#     def __init__(self):
#         super().__init__()
#         print("You are child")

# child = Child()

class A:
   def __init__(self):
       print("Initializing A")
class B(A):
   def __init__(self):
       super().__init__()
       print("Initializing B")
class C(A):
   def __init__(self):
       super().__init__()
       print("Initializing C")
class D(B, C):
   def __init__(self):
       super().__init__()
       print("Initializing D")

       
d = D()