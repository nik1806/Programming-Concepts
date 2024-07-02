

color = "Red"

class Vehicle:
    # initialize / constructor
    def __init__(self, new_color):
        # attributes
        self.color = new_color
        
    # methods
    def get_color(self):
        return self.color
    
    def set_color(self, new_color):
        self.color = new_color

# instantiate an object
car = Vehicle("Blue") # set variable value at instantiation
print(car.get_color())

car.set_color("White") # set color
print(car.get_color()) # get new color value