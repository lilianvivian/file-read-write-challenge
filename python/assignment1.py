# Assignment 1: Design Your Own Class! 🏗️

# A Smartphone class with attributes and methods
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours

    def call(self, number):
        return f"{self.brand} {self.model} is calling {number}..."

    def browse(self, website):
        return f"{self.brand} {self.model} is browsing {website}."

    def __str__(self):
        return f"Smartphone: {self.brand} {self.model}, Battery life: {self.battery_life} hours"


# Inheritance: GamingSmartphone (child of Smartphone)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery_life, cooling_system):
        super().__init__(brand, model, battery_life)
        self.cooling_system = cooling_system

    def play_game(self, game):
        return f"{self.brand} {self.model} is playing {game} with {self.cooling_system} cooling."

    def __str__(self):
        return f"Gaming Smartphone: {self.brand} {self.model}, Battery: {self.battery_life}h, Cooling: {self.cooling_system}"


# Example usage
if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "Galaxy S24", 24)
    phone2 = GamingSmartphone("Asus", "ROG Phone 7", 30, "liquid-cooling")

    print(phone1)
    print(phone1.call("+254712345678"))
    print(phone1.browse("www.google.com"))

    print()
    print(phone2)
    print(phone2.play_game("PUBG Mobile"))
