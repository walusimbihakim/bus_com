
from datetime import datetime  
class Driver:
    def __init__(self, name, gender, address, contact):
        self.name = name
        self.gender = gender
        self.address = address
        self.contact = contact
    
    def __str__(self):
        return self.name
  
class Bus:
    def __init__(self, bus_no, model, capacity, license_expiry):
        self.bus_no = bus_no
        self.model = model
        self.capacity = capacity
        self.license_expiry = license_expiry # 2024-10-01
        self.status = "Free"
        self.drivers = []
    
    def assign_driver(self, driver):
        if len(self.drivers) < 2:
            self.drivers.append(driver)
        else:
            print("Bus Already has two drivers")
    
    def get_bus_drivers(self):
        for driver in self.drivers:
            print(driver)
               
    
    def __str__(self):
        return f"{self.model} - {self.bus_no}"
    
    def check_license_expiry(self):
        expiry_date = datetime.strptime(self.license_expiry, "%Y-%m-%d").date()
        
        current_date = datetime.now().date()
        
        if current_date <= expiry_date:
            return True
        else:
            return False

class Trip:
    def __init__(self, trip_no, trip_date, source, destination):
        self.trip_no = trip_no
        self.trip_date = trip_date
        self.source = source
        self.destination = destination
        
    def __str__(self):
        return f"{self.trip_no}: {self.source}-{self.destination} - {self.bus}"
        
    def assign_bus(self, bus):
        has_license = bus.check_license_expiry()
        
        if has_license:
            if bus.status == "Free":
                self.bus = bus
                self.bus.status = "On Trip"
                print(f"Trip assigned Bus {bus}")
            else:
                print(f"The bus {bus} is already assigned a Trip")
        else:
            print(f"Bus {bus} License has expired")