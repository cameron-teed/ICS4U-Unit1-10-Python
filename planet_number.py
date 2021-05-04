#!/usr/bin/env python3

# Created by: Cameron Teed
# Created on: 2021-05-04
# This program finds the location of the inputted planet in our solar system

# Import enumerators
from enum import Enum


class planet_enumerator(Enum):
    # The first planet
    MERCURY = 1
    # The second planet
    VENUS = 2
    # The thrid planet
    EARTH = 3
    # The forth planet
    MARS = 4
    # The fifth planet
    JUPITER = 5
    # The sixth planet
    SATURN = 6
    # The seventh planet
    URANUS = 7
    # The eigth planet
    NEPTUNE = 8


def enum_index(planet_enum):
    # Finds the coresponding number to the inputted planet
    planet_position = planet_enumerator[planet_enum]
    # Returns the planets number
    return planet_position.value


def main():
    # This program finds the number related to the inputted planet

    try:
        # Asks user to input a planet
        user_planet = input("Enter the planet name: \n")

        # Converts string to upercase
        planet_enum = user_planet.upper()

        # Calls on the function that finds the coresponding number
        final_position = enum_index(planet_enum)

        # Prints out the planet number
        print("\n" + str(user_planet) + " is planet number " + str(final_position)
              + " in the solar system.")
        print("\nDone")

    # Runs if someone enters something other than a planet
    except KeyError:
        print("\nInvalid input, please try again.")
        

if __name__ == "__main__":
    main()
