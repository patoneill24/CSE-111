#author: Patrick O'Neill
EARTH_ACCELERATION_OF_GRAVITY	= 9.80665 #constant for gravity
WATER_DENSITY = 998.2 #constant for water density
WATER_DYNAMIC_VISCOSITY = 0.0010016 #constant for water dynamic viscosity

def water_column_height(tower_height, tank_height):
    """
    calculates water column height based on the height of the tower and the height of the tank
    """
    water_column_height = tower_height + ((3 * tank_height)/4)
    return water_column_height

def pressure_gain_from_water_height(height):
    """
    calculates the pressure caused by gravity's pull
    """
    pressure = (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height)/ 1000
    return pressure


def pressure_loss_from_pipe(pipe_diameter,pipe_length,friction_factor,fluid_velocity):
    """
    calcuates the pressure lost because of the friction between the water and the walls of the pipe that it flows through 
    based on the length and diameter of the pipe, along with the friction factor and fluid velocity
    """
    pressure_loss = (-friction_factor * pipe_length * WATER_DENSITY * fluid_velocity ** 2)/(2000 * pipe_diameter)
    return pressure_loss


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """
    calculates the pressure lost from pipe fittings that cause 45 and 90 degree bends 
    in the pipeline based on the fluid velocity and the number of fittings
    """
    pressure_loss = (-0.04 * WATER_DENSITY * (fluid_velocity**2) * quantity_fittings)/2000
    return pressure_loss

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    calculates the reynolds number (unitneless number of the forces in a fluid that 
    is useful for predicting fluid flow in different situations)
    based on the hydraualic diameter and fluid velocity
    """
    reynolds = (WATER_DENSITY * hydraulic_diameter * fluid_velocity)/ WATER_DYNAMIC_VISCOSITY
    return reynolds

def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
    """
    calculates the water pressure getting lost when moving from a pipe with a larger diameter 
    into a pipe with a smaller diameter based on the diameters of the pipe, the fluid velocity,
    and the reynolds number
    """
    k = (0.1 + (50/reynolds_number)) * ((larger_diameter/smaller_diameter) ** 4 - 1)
    lost_pressure = -k * WATER_DENSITY * (fluid_velocity**2)/2000
    return lost_pressure

def kPa_to_psi(pressure):
    """
    convers kilopascals to pounds per square inch based on the pressure of a force in kilopascals
    """
    pressure_in_psi = pressure * 0.14503773773020923
    return pressure_in_psi

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    """
    This is the main function the calcuates and prints the water pressure in a house based on the hight of the water tower,
    the height of the water tank walls, length of supply pipe (all in meters by the way), the number of 90 degree angles
    in supply pipe, and the length of pipe from supply to house in meters as well. 
    """
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    pressure_in_psi = kPa_to_psi(pressure)


    print(f"Pressure at house: {pressure:.1f} kilopascals or {pressure_in_psi:.1f} pounds per square inch")


if __name__ == "__main__":
    main()

