r = int(input())
c = int(input())
m = int(input())

current_end = (r * c) % m
# print(current_end)

# populate row
def create_next_row():
    row = []
    global current_end
    for _ in range(c):
        if current_end == 0:
            current_end = m
        row.append(current_end)
        current_end -= 1
    row.reverse()
    return row

# initialize first two rows
bottom_row = create_next_row()
top_row = create_next_row()
# print(top_row)
# print(bottom_row)

# program loop
for _ in range(r - 1, 0, -1):
    next_row = []
    for i in range(len(bottom_row)):
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
    
    bottom_row = next_row
    if _ != 0:
        top_row = create_next_row()

print(min(bottom_row))