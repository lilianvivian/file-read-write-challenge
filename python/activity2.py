# Activity 2: Polymorphism Challenge! 🎭

# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


# Subclasses with polymorphism
class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road"


class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky"


class Boat(Vehicle):
    def move(self):
        return "⛵ Sailing on the water"


# Example usage
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat()]

    for v in vehicles:
        print(v.move())
