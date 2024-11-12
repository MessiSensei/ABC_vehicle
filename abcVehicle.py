from abc import ABC, abstractmethod

# Define the abstract Vehicle class
class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def drive(self):
        """This abstract method must be implemented by subclasses to define how the vehicle drives."""
        pass

    @abstractmethod
    def __str__(self):
        """Return a string representation of the vehicle."""
        pass

# Implement the Car subclass
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def drive(self):
        return f"Driving the car: {self.make} {self.model} ({self.year})"

    def __str__(self):
        return f"{self.year} {self.make} {self.model} with {self.num_doors} doors"

# Implement the Motorcycle subclass
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def drive(self):
        return f"Riding the motorcycle: {self.make} {self.model} ({self.year})"

    def __str__(self):
        return f"{self.year} {self.make} {self.model} with {self.num_wheels} wheels"

# Usage example
car = Car("Toyota", "Corolla", 2020, 4)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021, 2)

# Test drive and string representation
print(car.drive())  # Output: Driving the car: Toyota Corolla (2020)
print(car)          # Output: 2020 Toyota Corolla with 4 doors

print(motorcycle.drive())  # Output: Riding the motorcycle: Harley-Davidson Sportster (2021)
print(motorcycle)          # Output: 2021 Harley-Davidson Sportster with 2 wheels
