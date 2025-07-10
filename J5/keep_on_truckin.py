# CCC '07 J5
motels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]

minDist = int(input())
maxDist = int(input())
x = int(input())
if x > 0:
    for _ in range(x):
        motels.append(int(input()))
    motels.sort()

print(motels)

today = []
yesterday = [0]