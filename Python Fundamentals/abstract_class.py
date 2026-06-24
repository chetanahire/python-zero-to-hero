from abc import ABC, abstractmethod

# class MyTestClass(ABC):
#     pass


from math import pi

class Shape(ABC):
    """
    Abstract base class for geometric shapes.
    Requires subclasses to implement:
      - area (read-only property)
      - perimeter (read-only property)
    """

    @property
    @abstractmethod
    def area(self):
        """Read-only property: returns the area of the shape."""
        pass

    @property
    @abstractmethod
    def perimeter(self):
        """Read-only property: returns the perimeter of the shape."""
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self._radius = radius

    @property
    def area(self):
        return pi * self._radius ** 2

    @property
    def perimeter(self):
        return 2 * pi * self._radius


if __name__ == "__main__":
    try:
        # shape = Shape()  # ❌ Error: Can't instantiate abstract class
        rect = Rectangle(5, 3)
        circle = Circle(4)

        print(f"Rectangle: area={rect.area}, perimeter={rect.perimeter}")
        print(f"Circle: area={circle.area:.2f}, perimeter={circle.perimeter:.2f}")

        # rect.area = 100  # ❌ AttributeError: can't set attribute (read-only)
    except (TypeError, ValueError, AttributeError) as e:
        print(f"Error: {e}")
