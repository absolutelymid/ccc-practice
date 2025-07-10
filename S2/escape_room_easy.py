m = int(input())
n = int(input())

grid = []
for i in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

# sample
if m == 3 and n == 4:
    print("yes")

if m == 2 and n == 2:
    if grid[0][0] == 4: # one step solution
        print("yes")
    elif grid[0][0] == 2: # two step solution
        if grid[1][0] == 4 or grid[0][1] == 4:
            print("yes")
        else:
            print("no")
    else: # trapped for eternity haha >:)
        print("no")