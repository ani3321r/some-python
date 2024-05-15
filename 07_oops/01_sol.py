class car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand #when we give __xyz it becomes private
        self.__model = model
        car.total_car += 1

    def get_brand(self):
        return self.__brand #it is accessible only inside the class       

    def full_name(self):
        return f"{self.__brand} {self.__model}"  

    def fuel_type(self):
        return "petrol or diesel"  
    
    @staticmethod #due to this only class can access this, but not objects
    def general_des(): #in static method self is not required
        return "cars are awsome"
    
    @property #it makes the property of an object readonly
    def model(self):
        return self.__model

class ElectricCar(car):
    def __init__(self,brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "electric"      

car0 = ElectricCar("Tesla", "cybertruck", "200kwh")
# print(car0.full_name())

car("porsche", "918 spyder") 
# print(car1.__brand) #this will not work as private object is not accessible outside scope  
# print(car1.get_brand()) #this will work as we are calling the private object inside the function
# print(car1.model)
# print(car1.full_name())
print(car0.fuel_type()) #polymorphism, both have same object with different properties

car("tata", "safari")
# print(car2.model)
# print(car2.fuel_type())

car3 = car("porsche", "911 turbo s")

print(car.total_car) #we can access a property directly by calling by the class name

print(car.general_des())

print(car3.model) #due to the decorator we can't call the object, either we can use it as a property

# print(isinstance(car0, car))
# print(isinstance(car0, ElectricCar))


class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"
    
class electricCar2(Battery, Engine, car):
    pass

car4 = electricCar2("rivian", "r1t")
print(car4.battery_info())
print(car4.engine_info())


