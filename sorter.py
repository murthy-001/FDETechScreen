# sorter.py

# classify package into specific category

# inclusive threshoulds 

dim_bulky_limit = 150               # cm
volume_bulky_limit = 1000000        # cm^3
heavy_mass_limit = 20               # kg

# func to identify catagory (dimensions in cm and mass in kg)
def sort(width, height, length, mass):
    # basic measurements
    volume = width * height * length
    longest_side = max(width, height, length)

    is_bulky = volume >= volume_bulky_limit or longest_side >= dim_bulky_limit
    is_heavy = mass >= heavy_mass_limit

    # identifying appopriate stack category
    if is_bulky and is_heavy:
        return "REJECTED"           # both heavy and bulky

    if is_bulky or is_heavy:
        return "SPECIAL"            # either heavy or bulky
    
    return "STANDARD"               # neither 