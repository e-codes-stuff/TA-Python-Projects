class EncapsulatedExample:
    def __init__(self, public_data, protected_data, private_data):
        # Public attribute
        self.public_data = public_data
        # Protected attribute (indicated by a single underscore)
        self._protected_data = protected_data
        # Private attribute (indicated by double underscores)
        self.__private_data = private_data

    def get_protected_data(self):
        # Public method to access the protected attribute
        return self._protected_data

    def __get_private_data(self):
        # Private method to access the private attribute
        return self.__private_data

    def access_private_data(self):
        # Public method that internally uses a private method to access private data
        return self.__get_private_data()

    def set_private_data(self, new_value):
        # Public method to update the private attribute
        self.__private_data = new_value


# Creating an object of the class
example = EncapsulatedExample("Public Info", "Protected Info", "Private Info")

# Accessing public data
print("Public Data:", example.public_data)

# Accessing protected data through a public method
print("Protected Data:", example.get_protected_data())

# Accessing private data through a public method
print("Private Data:", example.access_private_data())

# Updating private data through a public method
example.set_private_data("Updated Private Info")

# Accessing the updated private data
print("Updated Private Data:", example.access_private_data())
