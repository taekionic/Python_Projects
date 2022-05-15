class aerospace:  #creating a class that defines features all aerospace vehicles may have.
    vehicle_name = ""
    vehicle_model = ""
    vehicle_year = ""
    engine_thrust = ""
    exit_velocity = ""
    reusablity = ""

    def aerospace1(self):
        make = input("please enter make of the aerospace vehicle\n>>> ")
        model = input("please enter model of the aerospace vehicle\n>>> ")
        year = input("please enter aersopace vehicles manufacturing year\n>>> ")
        thrust = input("please enter rocket thrust\n>>> ")
        velocity = input("please enter exit velocity\n>>> ")
        reusability = input("please enter can or cannot\n>>> ").lower()
        print(f"The {make} {model} was manufactured in the year {year}. It has a maximum engine thrust of {thrust} and exits the atmosphere at {velocity}. It {reusability} be reused.")
  
class planes(aerospace): #creating a child class that includes all the attributes of its parent class, aerospace, but also traits that are unique to planes. 
    vehicle_name = ""
    vehicle_model = ""
    vehicle_year = ""
    wingspan = ""
    engine = ""
    maximum_altitude = ""

    def aerospace1(self):
        make = input("please enter make of the plane\n>>> ")
        model = input("please enter model of the plane\n>>> ")
        year = int(input("please enter plane's manufacturing year\n>>> "))
        wingspan = int(input("please enter wingspan in feet!\n>>> "))
        engine = input("please enter engine type\n>>> ")
        maximum_altitude = int(input("please enter maximum flight altitude\n>>> "))
        print(f"The {make} {model} was manufactured in the year {year}. It has a wingspan of {wingspan} feet and boasts a powerful {engine}. It can reach a maximum height of {maximum_altitude}")
    

class helicopters(aerospace): #creating a child class that includes all the attributes of its parent class, aerospace, but also traits that are unique to planes. 
    vehicle_name = ""
    vehicle_model = ""
    vehicle_year = ""
    rotor_radius = ""
    horsepower = ""

    def aerospace1(self):
        make = input("please enter make of the helicopter\n>>> ")
        model = input("please enter model of the helicopter\n>>> ")
        year = input("please enter helicopter's year\n>>> ")
        radius = input("please enter blade radius of the vehicle\n>>> ")
        horsepower = int(input("please enter can or cannot\n>>> "))
        print(f"The {make} {model} was manufactured in the year {year}. It has a rotor radius of {radius}, which is powered by a {horsepower} horsepower engine!.")



if __name__ == "__main__":
    rocket = aerospace()
    print(rocket.aerospace1())

    plane = planes()
    print(plane.aerospace1())

    helicopter = helicopters()
    print(helicopter.aerospace1())
