# - What Are Mixins?
# A mixin is a class designed to provide specific methods or behaviors to other classes through multiple inheritance, 
# but it is not meant to stand alone or represent an "is-a" relationship 

# - Mixins are typically:

# Stateless: They do not maintain their own instance variables.
# Focused: Each mixin addresses a single responsibility or behavior.
# Composable: Multiple mixins can be combined to extend a class’s functionality.
# For example, a LoggingMixin can add logging capabilities to any class without altering its core behavior.

# - Mixins vs Traditional Inheritance
# Traditional inheritance models an is-a relationship, 
# where a subclass extends a parent class and inherits its state and behavior. Mixins, in contrast:

# Provide behavioral extensions without forming a deep hierarchy.
# Avoid the rigidity of multi-level inheritance trees.
# Allow code reuse across unrelated classes without duplicating methods.

# While mixins rely on multiple inheritance in Python, 
# they are conceptually closer to composition, 
# because they let you "mix in" functionality rather than forcing a strict parent-child relationship 

# - Composition Over Inheritance
# The composition over inheritance principle encourages designing classes by combining 
# smaller components (has-a relationships) rather than relying solely on inheritance (is-a relationships),

# - Benefits include:

# Flexibility: Components can be swapped or extended at runtime.
# Maintainability: Changes in one component do not ripple through a rigid hierarchy.
# Modularity: Each component or mixin handles a single concern, making code easier to test and reuse.
# For instance, instead of creating multiple subclasses for every combination of behaviors, you can compose a class from reusable mixins like Flyable, Swimmable, or SoundEmitter.

# Best Practices for Using Mixins
# Behavior, Not State: Mixins should operate on the host class’s state, not maintain their own.
# Single Responsibility: Each mixin should encapsulate one behavior.
# Dependency Awareness: Mixins can assume certain attributes exist in the host class but should not define them.
# Avoid Standalone Use: Mixins are meant to be combined with other classes, not instantiated directly 

# - Summary
# Mixins provide a modular, reusable way to extend class behavior, 
# while composition over inheritance emphasizes building classes from interchangeable components. 
# Together, they allow developers to write flexible, maintainable, 
# and DRY code, avoiding the pitfalls of deep inheritance hierarchies and rigid type relationships.


class LoggingMixin:
    def log(self, message):
        print(f"[LOG] : ", message)

class SerializationMixin:
    def serialize(self):
        import json
        return json.dumps(self.__dict__)

class User (LoggingMixin, SerializationMixin):
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_info(self):
        self.log(f"Displaying information for : {self.username}")
        return f"UserName : {self.username}, Email : {self.email}"


if __name__ == "__main__":
    user = User("Sam", "sam@example.com")
     
    # Call method from the LoggingMixin
    user.log("This is a log message")

    # Call main class method
    print(user.display_info())

    # Call method from the SerializationMixin
    print("Serialized data:", user.serialize())