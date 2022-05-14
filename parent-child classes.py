class aerospace:  #creating a class that defines features all aerospace vehicles may have. 
    def __init__(self, vehicle_name,vehicle_model,vehicle_year):
        self.vehicle_name = vehicle_name,
        self.vehicle_model = vehicle_model,
        self.vehicle_year = vehicle_year
    
  
class planes(aerospace): #creating a child class that includes all the attributes of its parent class, aerospace, but also traits that are unique to planes. 
    def __init__(self, wingspan, engine, maximum_altitude):
        self.wingspan = wingspan
        self.engine = engine
        self.maximum_altitude = maximum_altitude
    

class rockets(aerospace): #creating a child class that includes all the attributes of its parent class, aerospace, but also traits that are unique to planes. 
    def __init__(self, engine_thrust, exit_velocity, reusability):
        self.engine_thrust = engine_thrust
        self.exit_velocity = exit_velocity
        self.reusablity = reusability