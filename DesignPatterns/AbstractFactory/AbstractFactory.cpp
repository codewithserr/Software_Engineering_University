#include <iostream>

/**
 * Each distinct entity of an entity family should have a base interface. All
 * variants of the entity must implement this interface.
 */
class Airplane{
    public:
    virtual ~Airplane(){};
    virtual void UsefulFunction() const = 0;

};

/**
 * Concrete Entities are created by corresponding Concrete Factories.
 */
class HeavyAirplane : public Airplane {
    public:
    void UsefulFunction() const {
        std::cout << "The result of the entity Heavy Airplane.\n";
    }

};

class MediumAirplane : public Airplane {
    public:
    void UsefulFunction() const {
        std::cout << "The result of the entity Medium Airplane.\n";
    }
};

class LightAirplane : public Airplane {
    public:
    void UsefulFunction() const {
        std::cout << "The result of the entity Light Airplane.\n";
    }
};

// ############## //

/**
 * Here's the the base interface of another entity. All entities can interact
 * with each other, but proper interaction is possible only between entities of
 * the same concrete variant.
 */

class Helicopter{
      /**
   * Entity Helicopter is able to do its own thing...
   */
    public:
    virtual ~Helicopter(){};
    virtual void UsefulFunction() const = 0;
    /**
   * ...but it also can collaborate with the Airplane.
   *
   * The Abstract Factory makes sure that all products it creates are of the
   * same variant and thus, compatible.
   */
    virtual void AnotherUsefulFunction(const Airplane &collaborator) const = 0;

};

class HeavyHelicopter : public Helicopter {
    public:
    void UsefulFunction() const {
        std::cout << "The result of the entity Heavy Helicopter.\n";
    }

    /**
   * The variant, Heavy Helicopter, is only able to work correctly with the variant,
   * Heavy Airplane. Nevertheless, it accepts any instance of HeavyAirplane as an
   * argument.
   */   
    void AnotherUsefulFunction(const Airplane &collaborator) const override {
        collaborator.UsefulFunction();
    }
};

class MediumHelicopter : public Helicopter {
    public:
    void UsefulFunction() const {
        std::cout << "The result of the entity Medium Helicopter.\n";
    }
    /**
   * The variant, MEdium Helicopter, is only able to work correctly with the variant,
   * Medium Airplane. Nevertheless, it accepts any instance of MediumAirplane as an
   * argument.
   */
    void AnotherUsefulFunction(const Airplane &collaborator) const override {
        collaborator.UsefulFunction();
    }  
};

class LightHelicopter : public Helicopter {
    public:
    void UsefulFunction() const {
        std::cout << "The result of the entity Light Helicopter.\n";
    }
     /**
   * The variant, Light Helicopter, is only able to work correctly with the variant,
   * Light Airplane. Nevertheless, it accepts any instance of LightAirplane as an
   * argument.
   */
    void AnotherUsefulFunction(const Airplane &collaborator) const override {
        collaborator.UsefulFunction();
    } 
};

/**
 * The Abstract Factory interface declares a set of methods that return
 * diffeten abstract entities. These entities are called a family, and are
 * related by a high-level theme or concept. Entities of one family are usually
 * able to collaborate among themselves. A family of entities may have several
 * variants, but the entities of one varian are incompatible with entities of
 * another.
*/
class AbstractFactory {
 public:
    virtual ~AbstractFactory(){};
    virtual Airplane *CreateAirplane() const = 0;
    virtual Helicopter *CreateHelicopter() const = 0;
};

/**
 * Concrete Factories produce a family of entities that belong to a single
 * variant. The factory guarantees that resulting entities are compatible. Note
 * that signatures of the Concrete Factory's methods return an abstract entity,
 * while inside the method a concrete entity is instantiated.
 */

class HeavyEntityFactory : public AbstractFactory {
    public:
        Airplane *CreateAirplane() const override{
            return new HeavyAirplane();
        }

        Helicopter *CreateHelicopter() const override {
            return new HeavyHelicopter();
        }
};

/**
 * Each Concrete Factory has a corresponding entity variant.
 */
class MediumEntityFactory : public AbstractFactory {
 public:
  Airplane *CreateAirplane() const override {
    return new MediumAirplane();
  }
  Helicopter *CreateHelicopter() const override {
    return new MediumHelicopter();
  }
};

/**
 * The client code works with factories and entities only through abstract
 * types: AbstractFactory and AbstractProduct. This lets you pass any factory or
 * product subclass to the client code without breaking it.
 *
 */
void ClientCode(const AbstractFactory &factory)
{
    const Airplane *product_a = factory.CreateAirplane();
    const Helicopter *product_b = factory.CreateHelicopter();
    product_b->UsefulFunction();
    product_b->AnotherUsefulFunction(*product_a);
    delete product_a;
    delete product_b;
}

int main()
{  
    std::cout << "Client: Testing client code with the first factory type:\n";
    HeavyEntityFactory *f1 = new HeavyEntityFactory();
    ClientCode(*f1);
    delete f1;

    std::cout <<std::endl;

    std::cout << "Client: Testing same  client code with the second factory type:\n";
    MediumEntityFactory *f2 = new MediumEntityFactory();
    ClientCode(*f2);
    delete f2;
}
