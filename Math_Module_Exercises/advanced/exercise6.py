import math

# Approximate radius of Earth in km
R = 6371.0

lat1 = math.radians(float(input("Latitude 1: ")))
lon1 = math.radians(float(input("Longitude 1: ")))
lat2 = math.radians(float(input("Latitude 2: ")))
lon2 = math.radians(float(input("Longitude 2: ")))

d = math.acos(math.sin(lat1)*math.sin(lat2) + math.cos(lat1)*math.cos(lat2)*math.cos(lon2-lon1)) * R
print("Distance between coordinates:", round(d, 2), "km")
