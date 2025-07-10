# CCC '10 S1
n = int(input())
top = (None, 0)
second_top = (None, 0)

for _ in range(n):
    computer = input().split()
    name = computer[0]
    r = int(computer[1])
    s = int(computer[2])
    d = int(computer[3])
    value = 2 * r + 3 * s + d
    if value > top[1]: # if current value is greater than current 1st
        second_top = list(top)
        top = (name, value)
    elif value == top[1]: # if current value is equal than current 1st
        if name < top[0]:
            second_top = list(top)
            top = (name, value)
        if value == second_top[1]:
            if name < top[0]:
                second_top = (name, value)
        elif value > second_top[1]:
            second_top = (name, value)  
    elif value > second_top[1]:
        second_top = (name, value)
    elif value == second_top[1]:
        if name < second_top[0]:
            second_top = (name, value)

if top[0] == None:
    pass
else:
    print(top[0])
if second_top[0] == None:
    pass
else:
    print(second_top[0])