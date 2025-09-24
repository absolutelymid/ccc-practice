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
    distances = []
    
    for i in range(r):
        city.append(list(input()))
    print(city)
    for i in range(r):
        row = []
        for j in range(len(city[0])):
            if city[i][j] != '*':
                row.append(0)
            else:
                row.append(-1)
        distances.append(row)
    distances[-1][-1] = 1
    print(distances)
    
    # solves the problem
    # the program goes through the city backwards so that dead ends can be caught
    for i in range(len(city) - 1, 0, -1): # rows
        for j in range(len(city[0]) - 1, 0, -1): # cell
            # check all four cells
            # top city[i - 1][j]
            try:
                if distances[i - 1][j] != -1:
                    inter = city[i - 1][j]
                    if intersection_allowed(inter, "UP"):
                        if distances[i - 1][j] == 0:
                            distances[i - 1][j] = distances[i][j] + 1
            except:
                pass
            # bottom city[i + 1][j]
            try:
                if distances[i + 1][j] != -1:
                    inter = city[i + 1][j]
                    if intersection_allowed(inter, "DOWN"):
                        if distances[i + 1][j] == 0:
                            distances[i + 1][j] = distances[i][j] + 1
            except:
                pass
            # left city[i][j - 1]
            try:
                if distances[i][j - 1] != -1:
                    inter = city[i][j - 1]
                    if intersection_allowed(inter, "LEFT"):
                        if distances[i][j - 1] == 0:
                            distances[i][j - 1] = distances[i][j] + 1
            except:
                pass
            # right city[i][j + 1]
            try:
                if distances[i][j + 1] != -1:
                    inter = city[i][j + 1]
                    if intersection_allowed(inter, "RIGHT"):
                        if distances[i][j + 1] == 0:
                            distances[i][j + 1] = distances[i][j] + 1
            except:
                pass

for i in distances:
    print(i)