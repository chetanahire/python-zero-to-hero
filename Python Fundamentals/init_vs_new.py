# In Python, __new__ is the method that actually creates the object, 
# while __init__ only initializes it after creation.

# Here’s the breakdown:
# -----------------------------------------------------------------------------------------------------------------------
# Method	    Purpose	                        When Called	                Return Value
# -----------------------------------------------------------------------------------------------------------------------
# __new__	    Creates and returns             Before __init__	            Must return the
#               a new instance of the class.	                            new object (usually via super().__new__(cls))
# __init__	    Initializes the                 Immediately after __new__	Returns None                            
#               already created instance.	  
 
# When we create object
# obj = MyClass(args)

# Python internally does:
# Calls MyClass.__new__(cls, args) → creates the object.
# Calls MyClass.__init__(obj, args) → initializes the object.  

class MyClass:
    def __new__(cls, *args, **kwargs):
        print("From __new__ method")
        # Calling the parent class's __new__ method to create the instance
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        # This method initializes the object after it's created
        print(f"{value}")
        self.value = value

# Create an instance of MyClass
obj = MyClass(10)
