# Define the parent class
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    # Method to be overridden by child classes
    def display_info(self):
        return f"This is a {self.brand} vehicle, made in {self.year}."


class Car(Vehicle):
    def __init__(self, brand, year, model, doors):
        # Calling the parent class constructor
        super().__init__(brand, year)
        # Child-specific attribute
        self.model = model
        # Child-specific attribute
        self.doors = doors

    # Overriding the parent class method
    def display_info(self):
        return f"This is a {self.brand} {self.model}, made in {self.year} with {self.doors} doors."


class Motorcycle(Vehicle):
    def __init__(self, brand, year, engine_type, has_sidecar):
        # Calling the parent class constructor
        super().__init__(brand, year)
        # Child-specific attribute
        self.engine_type = engine_type
        # Child-specific attribute
        self.has_sidecar = has_sidecar

    # Overriding the parent class method
    def display_info(self):
        sidecar_info = "with a sidecar" if self.has_sidecar else "without a sidecar"
        return f"This is a {self.brand} motorcycle, made in {self.year}, {sidecar_info}, engine type: {self.engine_type}."


# Example usage
car = Car("Toyota", 2020, "Camry", 4)
motorcycle = Motorcycle("Harley Davidson", 2018, "V-Twin", False)

# Displaying information using the overridden methods
car_info = car.display_info()
motorcycle_info = motorcycle.display_info()

car_info, motorcycle_info
