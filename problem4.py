#Problem 4 (Medium): Smart Thermostat System
class Thermostat:
    min_temp = 15.0
    max_temp = 30.0
    device_count = 0
    def __init__(self, location, initial_temp):
        self.location = location
        self.current_temp = initial_temp
        if initial_temp >= Thermostat.min_temp and \
            initial_temp <= Thermostat.max_temp:
            self.current_temp = initial_temp 
            print("Temp set success")
        else:
            self.current_temp = Thermostat.min_temp
            print("Out of range")
        self.readings = [self.current_temp]
    def set_temperature(self, new_temp):
        if Thermostat.min_temp <= new_temp <= Thermostat.max_temp:
            self.current_temp = new_temp
            self.readings.append(new_temp)
        else:
            print("Invalid temperature")
    def  get_average_temp(self):
        lenth = len(self.readings)
        if lenth == 0:
            return 0
        average = sum(self.readings) / lenth
    def display_status(self):
        print(f"Location: {self.location}, temp: {self.current_temp} ,"
              f"Reading count: {len(self.readings)}, Average: {self.get_average_temp}")    
    def is_comfortable(self):
        if 20 <= self.current_temp <= 25:
            print("Comfortable temperature")
        else:
            print("Uncomfortable")
living_room = Thermostat("Living Room", 22)
garage_room  = Thermostat("Garage", 10)
living_room.set_temperature(26.5)
living_room.set_temperature(35)
living_room.display_status()
garage_room.display_status()
living_room.is_comfortable()









