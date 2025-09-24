# CCC '08 S3


def intersection_allowed(inter, dir):
    if inter == '*':
        return False
    elif inter == '+':
        return True
    elif inter == '-':
        if dir == "LEFT" or dir == "RIGHT":
            return True
        else:
            return False
    elif inter == '|':
        if dir == "UP" or dir == "DOWN":
            return True
        else:
            return False
        

t = int(input())

for _ in range(t):
    # creates grids and stuff
    r = int(input())
    c = int(input())
    
    city = []
    dists = []
    
    for i in range(r):
        city.append(list(input()))
    print(city)
    for i in range(r):
        dists.append([0] * c)
    print(dists)
    
    # solves the problem
    for i in range(len(city) - 1, 0, -1): # rows
        for j in range(len(city[0]) - 1, 0, -1): # cell
            # check all four cells
            # top city[i - 1][j]
            try:
                inter = city[i - 1][j]
                if intersection_allowed(inter, "UP"):
                    if dists[i - 1][j] == 0:
                        dists[i - 1][j] = dists[i][j] + 1
            except:
                pass
            # bottom city[i + 1][j]
            try:
                inter = city[i + 1][j]
                if intersection_allowed(inter, "DOWN"):
                    if dists[i + 1][j] == 0:
                        dists[i + 1][j] = dists[i][j] + 1
            except:
                pass
            # left city[i][j - 1]
            try:
                inter = city[i][j - 1]
                if intersection_allowed(inter, "LEFT"):
                    if dists[i][j - 1] == 0:
                        dists[i][j - 1] = dists[i][j] + 1
            except:
                pass
            # right city[i][j + 1]
            try:
                inter = city[i][j + 1]
                if intersection_allowed(inter, "RIGHT"):
                    if dists[i][j + 1] == 0:
                        dists[i][j + 1] = dists[i][j] + 1
            except:
                pass

print(dists)