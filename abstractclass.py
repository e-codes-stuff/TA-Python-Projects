from abc import ABC, abstractmethod


# Abstract class
class AbstractExample(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def abstract_method(self):
        # This is an abstract method that needs to be implemented by any subclass
        pass

    def regular_method(self):
        # This is a regular method which is already implemented
        print(f"Regular method called with data: {self.data}")


# Child class that implements the abstract method
class ChildExample(AbstractExample):
    def abstract_method(self):
        # Implementing the abstract method
        print(f"Abstract method implemented with data: {self.data}")


# Creating an object of the child class
example = ChildExample("Sample Data")

# Using the abstract method - implemented in the child class
example.abstract_method()

# Using the regular method - inherited from the parent class
example.regular_method()
