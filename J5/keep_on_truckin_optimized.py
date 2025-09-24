# CCC '07 J5
# uses dictionaries to limit the size of lists for some of the later test cases
motels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]

minDist = int(input())
maxDist = int(input())
x = int(input())
if x > 0:
    for _ in range(x):
        motels.append(int(input()))
    motels.sort()

today = {}
yesterday = {0: 1}

while True:
    for start in yesterday:
        for i in range(yesterday[start]):
            if start != 7000:
                today_min = minDist + start
                today_max = maxDist + start
                # check each hotel
                for motel in motels:
                    if today_min <= motel <= today_max:
                        if motel in today:
                            today[motel] += 1
                        else:
                            today[motel] = 1
    
    # if no paths exist
    if len(today) == 0:
        paths = 0
        break
    # if every path has reached the end of the highway
    finish = True
    for i in today:
        if i != 7000:
            finish = False
    if finish:
        paths = len(today)
        break
    
    # reset list
    yesterday = dict(today)
    today = {}

print(paths)