# Parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Child class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, seating_capacity):
        super().__init__(brand, model)  # Calling the constructor of the parent class
        self.fuel_type = fuel_type  # Additional attribute specific to Car
        self.seating_capacity = seating_capacity  # Additional attribute specific to Car

# Another child class inheriting from Vehicle
class Motorcycle(Vehicle):
    def __init__(self, brand, model, engine_cc, has_sidecar):
        super().__init__(brand, model)  # Calling the constructor of the parent class
        self.engine_cc = engine_cc  # Additional attribute specific to Motorcycle
        self.has_sidecar = has_sidecar  # Additional attribute specific to Motorcycle

# Example usage
car = Car("Toyota", "Corolla", "Petrol", 5)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 750, False)

# Print attributes to demonstrate
print("Car details:", car.brand, car.model, car.fuel_type, car.seating_capacity)
print("Motorcycle details:", motorcycle.brand, motorcycle.model, motorcycle.engine_cc, motorcycle.has_sidecar)
