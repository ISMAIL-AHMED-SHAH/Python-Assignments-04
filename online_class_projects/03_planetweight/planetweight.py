

MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14
EARTH_GRAVITY = 1.0


# earthweight = float(input("Enter a weight on Earth: "))
# planet = input("Enter a planet name: ").strip().lower()
# # mars_weitht = round(earthweight * 0.378, 2)

# # print(f"weight on Mars: {mars_weitht}")
# if planet == "mercury":
#     print(f"Weight on {round(earthweight * MERCURY_GRAVITY, 2)}")
# elif planet == "venus":
#     print(f"Weight on {round(earthweight * VENUS_GRAVITY, 2)}")
# elif planet == "mars":
#     print(f"Weight on {round(earthweight * MARS_GRAVITY, 2)}")
# elif planet == "jupiter":
#     print(f"Weight on {round(earthweight * JUPITER_GRAVITY, 2)}")
# elif planet == "saturn":
#     print(f"Weight on {round(earthweight * SATURN_GRAVITY, 2)}")
# elif planet == "uranus":
#     print(f"Weight on {round(earthweight * URANUS_GRAVITY, 2)}")
# elif planet == "neptune":
#     print(f"Weight on {round(earthweight * NEPTUNE_GRAVITY, 2)}")
# elif planet == "earth":
#     print(f"Weight on {earthweight}")
# else:
#     print("Invalid planet name")


# Planetary gravity multipliers

# Dictionary with planetary gravity multipliers

gravity_factors = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Get user input
earth_weight = float(input("\nEnter a weight on Earth: "))
planet = input("\nEnter a planet: ").strip().capitalize()

# Check if planet exists in dictionary
if planet in gravity_factors:
    planet_weight = round(earth_weight * gravity_factors[planet], 2)
    print(f"\nThe equivalent weight on {planet}: {planet_weight}\n")
else:
    print("\nInvalid planet name!\n")



# Planetary gravity multipliers

def main():
    earth_weight_str = input("\nEnter a weight on Earth : ")
    earth_weight = float(earth_weight_str)
    planet = input("\nEnter a planet: ").strip().capitalize()

    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    elif planet == "Neptune":
        gravity_constant = NEPTUNE_GRAVITY
    elif planet == "Earth":
        gravity_constant = EARTH_GRAVITY
    else:
        print("\nInvalid planet name!")

    planet_weight = round(earth_weight * gravity_constant, 2)
    print(f"\nThe equivalent weight on {planet}: {planet_weight}\n")

if __name__ == '__main__':
    main()