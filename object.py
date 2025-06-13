class car:
def_init_(self,brand,speed)
self.brand=brand
self.speed=speed
def display(self):
    print(f"brand:{self.brand},speed:{self.speed}km/h")
def create_car():
    car1=car("Toyota",180)
    return car1
my_car=create_car()
my_car.display()
