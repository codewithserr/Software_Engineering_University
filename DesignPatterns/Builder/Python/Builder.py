from abc import ABC, abstractmethod
import numpy as np

 # It makes sense to use the Builder pattern only when your products are quite
 # complex and require extensive configuration.
 #
 # Unlike in other creational patterns, different concrete builders can produce
 # unrelated products. In other words, results of various builders may not
 # always follow the same interface.


class Aircraft():
    # Define the parts vector of the aircraft
    def __init__(self) -> None:
        self.parts_ = []

    # Create a method for listing parts of the aircraft
    def ListParts(self):
        print("Product Parts: ")
        for i in range(len(self.parts_)):
            if(self.parts_[i] == self.parts_[-1]):
                print(self.parts_[i], end="")
            else:
                print(self.parts_[i] + ' , ', end="")
        print('\n')

# The Builder interface specifies methods for creating the different parts of
# the Product objects.

class Builder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def ProducePartA(self)->None:
        pass

    @abstractmethod
    def ProducePartB(self)->None:
        pass

    @abstractmethod
    def ProducePartC(self)->None:
        pass

# The Concrete Builder classes follow the Builder interface and provide
# specific implementations of the building steps. Your program may have several
# variations of Builders, implemented differently.

class ConcreteBuilder1(Builder):
    Aircraft = Aircraft()

    # A fresh builder instance should contain a blank product object, which is
    # used in further assembly.

    def __init__(self):
        self.reset()

    def __del__(self):
        self.reset()

    def reset(self):
        self.aircraft = Aircraft()

    # All production steps work with the same product instance.
    def ProducePartA(self) -> None:
        self.aircraft.parts_.append("Part A1")

    def ProducePartB(self) -> None:
        self.aircraft.parts_.append("Part B1")

    def ProducePartC(self) -> None:
        self.aircraft.parts_.append("Part C1")

    # This method in Python returns the current aircraft 
    # object and then resets the constructor 
    # (in this case, the reset() method) to prepare for the
    # construction of a new object
    def GetProduct(self):
        result = self.aircraft
        self.reset()
        return result
    
# The Director is only responsible for executing the building steps in a
# particular sequence. It is helpful when producing products according to a
# specific order or configuration. Strictly speaking, the Director class is
# optional, since the client can control builders directly.
class Director():
    def __init__(self):
        self.builder = None
    # The Director works with any builder instance that the client code passes
    #  to it. This way, the client code may alter the final type of the newly
    #  assembled product.

    def Set_Builder(self, builder):
        self.builder = builder

    # The Director can construct several product variations using the same
    # building steps.  

    def BuildMinimalViableProduct(self):
        self.builder.ProducePartA()

    def BuildFullFeaturedProduct(self):
        self.builder.ProducePartA()
        self.builder.ProducePartB()
        self.builder.ProducePartC()

# The client code creates a builder object, passes it to the director and then
# initiates the construction process. The end result is retrieved from the
# builder object.

def ClientCode(director: Director):
    builder = ConcreteBuilder1()
    director.Set_Builder(builder)

    print("Standard basic product")
    director.BuildMinimalViableProduct()

    p = builder.GetProduct()
    p.ListParts()
    del p

    print("Standard Full product")
    director.BuildFullFeaturedProduct()
    p = builder.GetProduct()
    p.ListParts()
    del p

    # Remember, the Builder pattern can be used without 
    # a Director class.

    print("Custom product")
    builder.ProducePartA()
    builder.ProducePartB()
    p = builder.GetProduct()
    p.ListParts()

    del p
    del builder

def Application():
    director = Director()
    ClientCode(director)
    del director

# Punto de entrada principal
if __name__ == "__main__":
    # Run the application
    Application()
