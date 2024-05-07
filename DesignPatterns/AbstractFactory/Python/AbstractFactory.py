from abc import ABC, abstractmethod
# Each distinct entity of an entity family should have a base interface. All
# variants of the entity must implement this interface.
 
class Airplane(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def UsefulFunction(self) -> None:
        pass

#  Concrete Entities are created by corresponding Concrete Factories.
class HeavyAirplane(Airplane):
    def UsefulFunction(self):
        print("The result of the entity Heavy Airplane")

class MediumAirplane(Airplane):
    def UsefulFunction(self):
        print("The result of the entity Medium Airplane")

class LightAirplane(Airplane):
    def UsefulFunction(self):
        print("The result of the entity Light Airplane")

# Here's the the base interface of another entity. All entities can interact
# with each other, but proper interaction is possible only between entities of
# the same concrete variant.

class Helicopter(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    # Entity Helicopter is able to do its own thing...
    @abstractmethod
    def UsefulFunction(self) -> None:
        pass

   # ...but it also can collaborate with the Airplane.
   
   # The Abstract Factory makes sure that all products it creates are of the
   # same variant and thus, compatible.

    @abstractmethod
    def AnotherUsefulFunction(collaborator: Airplane) -> None:
        pass

class HeavyHelicopter(Helicopter):
    def UsefulFunction(self):
        print("The result of the entity Heavy Airplane")

   #The variant, Heavy Helicopter, is only able to work correctly with the variant,
   # Heavy Airplane. Nevertheless, it accepts any instance of HeavyAirplane as an
   # argument.   
    def AnotherUsefulFunction(collaborator: Airplane):
        collaborator.UsefulFunction()


class MediumHelicopter(Helicopter):
    def UsefulFunction(self):
        print("The result of the entity Medium Airplane")
    # The variant, Medium Helicopter, is only able to work correctly with the variant,
    # Medium Airplane. Nevertheless, it accepts any instance of HeavyAirplane as an
    # argument.
    def AnotherUsefulFunction(collaborator: Airplane):
        collaborator.UsefulFunction()

class LightHelicopter(Helicopter):
    def UsefulFunction(self):
        print("The result of the entity Light Airplane")
    # The variant, Light Helicopter, is only able to work correctly with the variant,
    # Light Airplane. Nevertheless, it accepts any instance of HeavyAirplane as an
    # argument.
    def AnotherUsefulFunction(collaborator: Airplane):
        collaborator.UsefulFunction()

# The Abstract Factory interface declares a set of methods that return
# diffeten abstract entities. These entities are called a family, and are
# related by a high-level theme or concept. Entities of one family are usually
# able to collaborate among themselves. A family of entities may have several
# variants, but the entities of one varian are incompatible with entities of
# another.

class AbstractFactory(ABC):
    @abstractmethod
    def CreateAirplane(self)->Airplane:
        pass

    @abstractmethod
    def CreateHelicopter(self)->Helicopter:
        pass

# Concrete Factories produce a family of entities that belong to a single
# variant. The factory guarantees that resulting entities are compatible. Note
# that signatures of the Concrete Factory's methods return an abstract entity,
# while inside the method a concrete entity is instantiated.

class HeavyEntityFactory(AbstractFactory):
    def CreateAirplane(self) -> Airplane:
        return HeavyAirplane()
    
    def CreateHelicopter(self) -> Helicopter:
        return HeavyHelicopter()
    

class MediumEntityFactory(AbstractFactory):
    def CreateAirplane(self) -> Airplane:
        return MediumAirplane()
    
    def CreateHelicopter(self) -> Helicopter:
        return MediumHelicopter()
    

# The client code works with factories and entities only through abstract
# types: AbstractFactory and AbstractProduct. This lets you pass any factory or
# product subclass to the client code without breaking it.

def ClientCode(factory: AbstractFactory):
    product_a = factory.CreateAirplane()
    product_b = factory.CreateHelicopter()

    product_b.UsefulFunction()
    product_b.AnotherUsefulFunction()

    del product_b
    del product_a

def Application():
    print("Client: Testing client code with the first factory type: ")
    f1 = HeavyEntityFactory()
    ClientCode(f1)
    del f1

    print("Client: Testing same  client code with the second factory type")
    f2 = MediumEntityFactory()
    ClientCode(f2)
    del f2

# Punto de entrada principal
if __name__ == "__main__":
    # Run the application
    Application()