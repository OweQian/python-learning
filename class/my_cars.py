from car import Car
from electric_car import ElectricCar

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(23500)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2024)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()