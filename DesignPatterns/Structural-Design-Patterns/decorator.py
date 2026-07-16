from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

class PlainCoffee(Coffee):
    def get_description(self):
        print("It's a plain coffee")
    
    def get_cost(self):
        return 2.0

class CoffeeDecorator(Coffee):
    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    def get_description(self):
        self.decorated_coffee.get_description()

    def get_cost(self):
        self.decorated_coffee.get_cost()

class MilkDecorator(CoffeeDecorator):
    def get_description(self):
        self.decorated_coffee.get_description()
        print("Milk added")
    
    def get_cost(self):
        milk_coffee_cost = self.decorated_coffee.get_cost() + 0.5
        print(f"Cost of milkcoffee is {milk_coffee_cost}")
        return milk_coffee_cost

class SugarDecorator(CoffeeDecorator):
    def get_description(self):
        self.decorated_coffee.get_description()
        print("Sugar added")
    
    def get_cost(self):
        sugar_coffee_cost = self.decorated_coffee.get_cost() + 0.25
        print(f"Cost of sugared coffee is {sugar_coffee_cost}")
        return sugar_coffee_cost
    

if __name__ == "__main__":
    coffee = PlainCoffee()
    milk_coffee = MilkDecorator(coffee)
    milk_coffee.get_description()
    milk_coffee.get_cost()
    sugar_milk_coffee = SugarDecorator(milk_coffee)
    sugar_milk_coffee.get_description()
    sugar_milk_coffee.get_cost()