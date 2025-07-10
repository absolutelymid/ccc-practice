r = int(input())
c = int(input())
m = int(input())

current_end = 1
top_row = []
bottom_row = []

# populate row
def create_next_row():
    row = []
    global current_end
    for _ in range(c):
        if current_end == m + 1:
            current_end = 1
        row.append(current_end)
        current_end += 1
    return row

# initialize first two rows
top_row = create_next_row()
bottom_row = create_next_row()

# program loop
for _ in range(r): # go through total number of rows
    next_row = []
    for i in range(len(top_row)):
        value = float('inf')
        # cell to the left
        try:
            if i - 1 == -1:
                cost = float('inf')
            else:
                cost = top_row[i] + bottom_row[i - 1]
            if cost < value:
                value = cost
        except: pass
        # cell to the right
        try:
            cost = top_row[i] + bottom_row[i + 1]
            if cost < value:
                value = cost
        except: pass
        # cell directly below
        cost = top_row[i] + bottom_row[i]
        if cost < value:
            value = cost
        # add to next row
        next_row.append(value)
    
    top_row = next_row
    bottom_row = create_next_row()

print(min(top_row))