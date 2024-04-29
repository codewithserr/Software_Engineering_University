#include <iostream>
/*
    The Entity interface implements all the operations that all concrete entities must
    implement.
*/
class Entity {
    protected:
        int AirSpeed;
        int GroundSpeed;
        int Altitude;
        int Heading;
        int GroundTrack;

    public:
        virtual ~Entity(){};
        virtual std::string Operation() const = 0;
        virtual void UpdateEntity() const = 0;
        virtual void InitEntity() const = 0;
        
};

/*
   Concrete Entities provide various implementations of the Product interface.
*/
class AirplaneEntity : public Entity {
    public:
        std::string Operation() const override{return "{Airplane Entity has been created.\n}";}
        void UpdateEntity() const override{ std::cout << "Logic for updating entity parameters.\n";}
        void InitEntity() const override{std::cout << "Initialice Airpleane parameters.\n";} 

};

class HelicopterEntity : public Entity {
    public:
    std::string Operation() const override{return "{Helicopter Entity has been created.\n}";}
    void UpdateEntity() const override{ std::cout << "Logic for updating entity parameters.\n";}
    void InitEntity() const override{std::cout << "Initialice Helicopter parameters.\n";} 


};

/*
    The Creator class declares the Factory method that is supposed to return an objecto of a Product Class. 
    The Creator's subclasses usually provide the implementation of this method
*/
class Creator {

    public:
        virtual ~Creator(){};
        virtual Entity* FactoryMethod() const = 0;
    /*
        Despite its name, the Creator's primary responsibility is not creating products. 
        Usually, it contais some core bussines logic that relies on Entity Objects, returned by the factory method. 
        Subclasses can indirectly change that business logic by overriding the factory method and returning
        a different type of Entity from it
    */

    void SomeOperation() const {
    //Call the factory method to create a Product Object
    Entity* entity = this->FactoryMethod();
    //Now, use the prodcut.
    std::string result = "Creator: the same creator's code has just worked with " + entity->Operation();
   }
};

/*
    Concrete creators override the factory method in order to change the resulting
    product type
*/
class AirplaneCreator : public Creator {
/*
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
*/
    public:
        Entity* FactoryMethod() const override {
            return new AirplaneEntity();
        }
};

class HelicopterCreator : public Creator {
    public:
        Entity* FactoryMethod() const override {
            return new HelicopterEntity();
        }
};

/*
    The client code works with an instace of a concrete creator, albeit
    through its base interface. As long as the client keeps working with the creator
    via the base interfacem you can pass it any creator's subclass.
*/

void CliendCode (const Creator& creator){

    // Create an entity Object using FactoryMethod from Creator Class
    Entity* entity = creator.FactoryMethod();

    // Call Entity (or its childs) methods
    entity->InitEntity();
    entity->UpdateEntity();

    // Delete the entity when no needed
    delete entity;
}


/**
 * The Application picks a creator's type depending on the configuration or
 * environment.
 */
int main()
{
    std::cout << "App: Launched with the AirplaneCreator.\n";
    Creator* Airplane = new AirplaneCreator();
    CliendCode(*Airplane);
    std::cout << std::endl;
    std::cout << "App: Launched with the HelicopterCreator.\n";
    Creator* Helicopter = new HelicopterCreator();
    CliendCode(*Helicopter);

    return 0;
}
