from abc import ABC, abstractmethod

#    The Entity Class implements all the operations that all concrete entities must
#    implement.

class Entity(ABC):
    #Using None for inheritance purposes. If not, I need to initalize
    #it later in AirplaneCreator and HelicopterCreator method
    def __init__(self, Airspeed = 0, GrounSpeed= 0, Altitude= 0,
                 Heading= 0, GroundTrack= 0):
        self.Airspeed = Airspeed
        self.GroundSpeed = GrounSpeed
        self.Altitude = Altitude
        self.Heading = Heading
        self.GroundTrack = GroundTrack
    @abstractmethod
    def Operation(self):
        print("Operation from Entity class")

    @abstractmethod
    def UpdateEntity(self):
        print("UpdateEntity from Entity class")

#    Concrete Entities provide various implementations of the Product interface.

class AirplaneEntity(Entity):
    def __init__(self, Airspeed=None, GroundSpeed=None, Altitude=None,
                 Heading=None, GroundTrack=None): 
        # Call Entity constructor with default values
        super().__init__(Airspeed, GroundSpeed, Altitude, Heading, GroundTrack)
        
    # Here we use polymorphism for overriding methods from father class
    def Operation(self):
        print("Operation from AirplaneEntity class")

    def UpdateEntity(self):
        print("UpdateEntity from AirplaneEntity class ")
    
class HelicopterEntity(Entity):
    def __init__(self, Airspeed=None, GroundSpeed=None, Altitude=None,
                 Heading=None, GroundTrack=None): 
        # Call Entity constructor with default values
        super().__init__(Airspeed, GroundSpeed, Altitude, Heading, GroundTrack)
        
    # Here we use polymorphism for overriding methods from father class
    def Operation(self):
        print("Operation from HelicopterEntity class")

    def UpdateEntity(self):
        print("UpdateEntity from HelicopterEntity class ")


# The Creator class declares the Factory method that is supposed to return an object of a Entity Class. 
# The Creator's subclasses usually provide the implementation of this method


# Despite its name, the Creator's primary responsibility is not creating entities. 
# Usually, it contais some core bussines logic that relies on Entity Objects, returned by the factory method. 
# Subclasses can indirectly change that business logic by overriding the factory method and returning
# a different type of Entity from it
#
class Creator(ABC):
    @abstractmethod
    def FactoryMethod(self)->Entity:
        pass

    def SomeOperation(self)->None:
        #Call the factory method to create a Product Object
        entity = self.FactoryMethod()
        
        #Now, use the product of factory method
        result = {f"Creator: the same creator's code has just worked with {entity.Operation()}"}


#    Concrete creators override the factory method in order to change the resulting
#    product type

class AirplaneCreator(Creator):
    def FactoryMethod(self) -> Entity:
        return AirplaneEntity()
    
class HelicopterCreator(Creator):
    def FactoryMethod(self) -> Entity:
        return HelicopterEntity()


#    The client code works with an instace of a concrete creator, albeit
#    through its base interface. As long as the client keeps working with the creator
#    via the base interfacem you can pass it any creator's subclass.

def ClientCode(creator: Creator):
    # Create an entity Object using FactoryMethod from Creator Class
    entity = creator.FactoryMethod()

    # Call Entity (or its childs) methods
    entity.Operation()
    entity.UpdateEntity()

    # Delete the entity when no needed
    del entity

#
# The Application picks a creator's type depending on the configuration or
# environment.
#

def Application():
    print("App: Launched with the AirplaneCreator.\n")
    Airplane = AirplaneCreator()
    ClientCode(Airplane)

    print("\n")

    print("App: Launched with the HelicopterCreator.\n")
    Airplane = HelicopterCreator()
    ClientCode(Airplane) 


# Punto de entrada principal
if __name__ == "__main__":
    # Run the application
    Application()