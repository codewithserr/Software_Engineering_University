#include <iostream>
#include <memory>
#include <unordered_map>

// Prototype Design Pattern
//
// Intent: Lets you copy existing objects without making your code dependent on
// their classes.

/* In this example, In the case of the air traffic management system, we could use the Prototype pattern to create different types of 
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
*/

enum AircraftType {
    COMMERCIAL = 0,
    CARGO,
    HELICOPTER,
    DRONE
};

/**
 * The example class that has cloning ability. We'll see how the values of field
 * with different types will be cloned.
 */

class Aircraft {
    protected:
    std::string aircraft_model_;
    float max_speed_;

    public:
    Aircraft() {};
    Aircraft(std::string aircraft_model) 
            : aircraft_model_(aircraft_model){};

    virtual ~Aircraft(){};
    virtual Aircraft *Clone() const = 0;
    virtual void Fly(float speed) {
        std::cout << aircraft_model_ << " flying at speed: " << speed << " knots." << std::endl;
    }
};

/*
 * CommercialAircraft  is a Sub-Class of Prototype and implement the Clone Method
 * In this example all data members of Prototype Class are in the Stack. If you
 * have pointers in your properties for ex: String* name_ ,you will need to
 * implement the Copy-Constructor to make sure you have a deep copy from the
 * clone method
 */

class CommercialAircraft  : public Aircraft {
    private:
        float max_speed_commercial_aircraft_;
    public:
    CommercialAircraft (std::string aircraft_model, float max_speed_commercial_aircraft) 
        : Aircraft(aircraft_model), max_speed_commercial_aircraft_(max_speed_commercial_aircraft) { }

    /*
   * Notice that Clone method return a Pointer to a new ConcretePrototype1
   * replica. so, the client (who call the clone method) has the responsability
   * to free that memory. If you have smart pointer knowledge you may prefer to
   * use unique_pointer here.
   */
    Aircraft *Clone() const override {
        return new CommercialAircraft(*this);
    }
};

class CargoAircraft : public Aircraft {

private:
    float max_speed_cargo_aircraft_;
public:
    CargoAircraft(std::string aircraft_model, float max_speed_cargo_aircraft)
        : Aircraft(aircraft_model), max_speed_cargo_aircraft_(max_speed_cargo_aircraft) {}

    Aircraft *Clone() const override {
        return new CargoAircraft(*this);
    }
};

/**
 * In AircraftFactory you have two concrete prototypes, one for each concrete
 * Aircraft class, so each time you want to create an Aircraft, you can use the
 * existing ones and clone those.
 */
class AircraftFactory  {
    private:
    std::unordered_map<AircraftType, Aircraft *, std::hash<int>> prototypes_;

    public:
    AircraftFactory() {
        prototypes_[AircraftType::COMMERCIAL] = new CommercialAircraft("Boeint 747 ", 570);
        prototypes_[AircraftType::CARGO] = new CargoAircraft("Boeint 777F ", 560);
    }

    /*
   * Be carefull of free all memory allocated. Again, if you have smart pointers
   * knowelege will be better to use it here.
   */
    ~AircraftFactory() {
        delete prototypes_[AircraftType::COMMERCIAL];
        delete prototypes_[AircraftType::CARGO];
    }

  /**
   * Notice here that you just need to specify the type of the prototype you
   * want and the method will create from the object with this type.
   */
    Aircraft *CreateAircraft(AircraftType  type) {
        return prototypes_[type]->Clone();
    }
};

void ClientCode(AircraftFactory &aircraft_factory)
{
    std::cout << "Creating commercial aircraft\n";

    Aircraft *aircraft = aircraft_factory.CreateAircraft(AircraftType::COMMERCIAL);
    aircraft->Fly(500);
    delete aircraft;

    std::cout << "\n";

    std::cout << "Creating prototype 2\n";

    aircraft = aircraft_factory.CreateAircraft(AircraftType::CARGO);
    aircraft->Fly(350);
    delete aircraft;
}



int main()
{   
    //Use of smart pointers allow us to not call the desctructor once finishing
    std::unique_ptr<AircraftFactory> aircraft_factory (new AircraftFactory());
    
    ClientCode(*aircraft_factory);

    return 0;
}