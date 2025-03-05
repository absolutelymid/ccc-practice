# CCC '06 S3

"""
Strategy
Consider each side of a building as an individual line segment
Find the POI of the side and the telephone line (using the slopes and stuff)
Check if POI is between the two ends of the side of the building, if yes then it intersects
"""

rx, ry, jx, jy = list(map(int, input().split()))
r = (rx, ry)
j = (jx, jy)
# slope of telephone line used
try: phone_m = (r[1] - j[1])/(r[0] - j[0])
except: phone_m = 0
phone_b = r[1] - phone_m * r[0]
n = int(input())
buildings = []
for i in range(n):
    building = list(map(int, input().split()))
    buildings.append(building)

block_count = 0
for building in buildings:
    building_copy = building
    n_points = building_copy[0]
    building_copy.pop(0)
    points = []
    for p in range(0, len(building_copy), 2):
        points.append((building_copy[p], building_copy[p + 1]))
    # look for intersections with each side
    for p in range(0, len(points)):
        try: p2 = points[p + 1]
        except: p2 = points[0]
        p1 = points[p]
        # linear equation: y = mx + b
        # slope formula: m = (y2 - y1)/(x2 - x1)
        try: building_m = (p2[1] - p1[1])/(p2[0] - p1[0])
        except: building_m = 0
        building_b = p1[1] - building_m * p1[0]
        try: poi_x = -(building_b - phone_b)/(building_m - phone_m)
        except: continue
        poi_y = building_m * poi_x + building_b
        poi = (poi_x, poi_y)
        # testing x values
        if r[0] <= poi[0] <= j[0] or j[0] <= poi[0] <= r[0]:
            # testing y values
            if r[1] <= poi[1] <= j[1] or j[1] <= poi[1] <= r[1]:
                block_count += 1
                break

print(block_count)