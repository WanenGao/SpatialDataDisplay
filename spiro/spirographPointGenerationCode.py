import math
import simplekml

# Spirograph parameters
R = 36
r = 9
a = 30

# Center coordinates (Longitude, Latitude)
center_longitude = -118.28544586411549
center_latitude = 34.020557835091076

# Calculate points
points = []
num_loops = 8
step = 0.01
t = 0
while t < num_loops * math.pi:
    x = (R + r) * math.cos((r / R) * t) - a * math.cos((1 + r / R) * t)
    y = (R + r) * math.sin((r / R) * t) - a * math.sin((1 + r / R) * t)
    
    # Scale down the x and y to convert to approximate degrees
    # This is a rough approximation, you may need to adjust the scaling factor
    scale_factor = 0.0001
    x *= scale_factor
    y *= scale_factor
    
    # Add the center offset to position correctly on the globe
    longitude = center_longitude + y
    latitude = center_latitude + x
    
    points.append((longitude, latitude))
    t += step

# Create a KML file
kml = simplekml.Kml()

# Add points to KML
for point in points:
    kml.newpoint(coords=[point])

# Save the KML
kml.save("spirograph.kml")

