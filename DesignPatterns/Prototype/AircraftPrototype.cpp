#include <iostream>
#include <memory>
#include <unordered_map>

// Prototype Design Pattern
//
// Intent: Lets you copy existing objects without making your code dependent on
// their classes.

enum AircraftType {
    COMMERCIAL = 0,
    CARGO,
    HELICOPTER,
    DRONE
};

