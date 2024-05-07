from abc import ABC, abstractmethod
from enum import Enum

"""
Prototype Design Pattern

 Intent: Lets you copy existing objects without making your code dependent on
 their classes.

In this example, In the case of the air traffic management system, we could use the Prototype pattern to create different types of 
aircraft, such as commercial airplanes, cargo planes, helicopters, drones, etc. Each type of aircraft has different 
characteristics and behaviors, but they also share some basic similarities.

By using the Prototype pattern, instead of creating a new instance of an aircraft class every time we need to add a 
new type to the system, we could simply clone an existing instance and adjust its characteristics as needed. 
This is useful because it allows us to leverage existing instances and modify them as required by the new type 
of aircraft, rather than building each type from scratch.

For example, if we need to add a new type of cargo plane to the air traffic management system, we could clone an 
instance of an existing cargo plane and adjust its cargo capacity and other specific characteristics of the new plane.
This saves us time and effort in creating and configuring new aircraft each time a new type needs to be incorporated 
into the air traffic management system.
"""

class AircraftType(Enum):
    COMMERCIAL = 1
    CARGO = 2
    HELICOPTER = 3
    DRONE = 4

# The example class that has cloning ability. We'll see how the values of field
# with different types will be cloned.
class Aircraft(ABC):
    def __init__(self, aircraft_model):
        self.aircraft_model_ = aircraft_model

    @abstractmethod
    def Clone(self)->None:
        pass

    @abstractmethod
    def fly(self, speed):
        pass
# CommercialAircraft  is a Sub-Class of Prototype and implement the Clone Method
#  In this example all data members of Prototype Class are in the Stack. If you
#  have pointers in your properties for ex: String* name_ ,you will need to
#  implement the Copy-Constructor to make sure you have a deep copy from the
#  clone method
class CommercialAircraft(Aircraft):
    def __init__(self, aircraft_model, max_speed_commercial_Aircraft_):
        super().__init__(aircraft_model) #From aircraf Class
        self.max_speed_commercial_Aircraft = max_speed_commercial_Aircraft_ # From commercial class

    def Clone(self)->Aircraft:
        return CommercialAircraft(self.aircraft_model_, self.max_speed_commercial_Aircraft)
    
    def fly(self, speed):
        print(self.aircraft_model_ + " flying at speed: " + str(speed) + " Knots")



class CargoAircraft(Aircraft):
    def __init__(self, aircraft_model, max_speed_cargo_Aircraft_):
        super().__init__(aircraft_model) #From aircraf Class
        self.max_speed_cargo_Aircraft = max_speed_cargo_Aircraft_ # From commercial class

    def Clone(self)->Aircraft:
        return CargoAircraft(self.aircraft_model_, self.max_speed_cargo_Aircraft)
    
    def fly(self, speed):
        print(self.aircraft_model_ + " flying at speed: " + str(speed) + " Knots")

# In AircraftFactory you have two concrete prototypes, one for each concrete
# Aircraft class, so each time you want to create an Aircraft, you can use the
# existing ones and clone those.
class AircraftFactory:

    def __init__(self):
        self.prototypes_ = {}

        self.prototypes_[AircraftType.COMMERCIAL] =CommercialAircraft("Boeing 747 ", 570)
        self.prototypes_[AircraftType.CARGO] = CargoAircraft("Boeing 777F ", 560)

    def CreateAircraft(self, type):
        return self.prototypes_[type].Clone()


def ClientCode(aircraft_factory: AircraftFactory):
    print("Creating commercial aircraft\n")

    aircraft = aircraft_factory.CreateAircraft(AircraftType.COMMERCIAL)
    aircraft.fly(500)
    del aircraft

    print("\n")

    print("Creating Cargo aircraft\n")

    aircraft = aircraft_factory.CreateAircraft(AircraftType.CARGO)
    aircraft.fly(350)
    del aircraft

def Application():
    aircraft_factory = AircraftFactory()
    ClientCode(aircraft_factory)

# Punto de entrada principal
if __name__ == "__main__":
    # Run the application
    Application()