# Find the distance between any two capital cities in the world

# DISTANCE CALCS
from math import radians, cos, sin, asin, sqrt
def distance(lat1, lat2, lon1, lon2):
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371
    return (c * r)


# GEOPY LIBRARY
from geopy.geocoders import Nominatim

# FIND COORDINATES
def get_coordinates(city):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(city)

    if location:
        return location.latitude, location.longitude
    else:
        print(f"Coordinates not found for {city}")
        return None

# CITIES (user input)
city1 = input("First location: type in 'City, Country': ")
city2 = input("Second location: type in 'City, Country': ")

# CITY1
capital_cities = [city1]
for city1 in capital_cities:
    coordinates = get_coordinates(city1)

    if coordinates:
        lat1 = coordinates[0]
        lon1 = coordinates[1]

# CITY2
capital_cities = [city2]
for city2 in capital_cities:
    coordinates = get_coordinates(city2)

    if coordinates:
        lat2 = coordinates[0]
        lon2 = coordinates[1]


# CITY1 and CITY2 into lat1/lat2/lon1/lon2
result = distance(lat1, lat2, lon1, lon2)

# PRINT DISTANCE BETWEEN THE TWO LOCATIONS
print("The distance between", city1, "and", city2, "is", int(result), "kms.")
