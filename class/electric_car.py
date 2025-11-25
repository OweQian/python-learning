from car import Car
from battery import Battery

class ElectricCar(Car):
  def __init__(self, make, model, year):
    super().__init__(make, model, year)
    self.battery = Battery()
    
  def describe_battery(self):
    print(f"This car has a {self.battery_size}-kWh battery.")