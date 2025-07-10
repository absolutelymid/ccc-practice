# CCC 25' J4
x = int(input())
days = [input() for _ in range(x)]

starts = []
ends = []

last_day = ''
for day in range(len(days)):
    if days[day] != last_day:
        if days[day] == 'S':
            starts.append(day)
        elif days[day] == 'P':
            ends.append(day)
        elif last_day == '':
            if days[day] == 'S':
                starts.append(day)
    last_day = days[day]
    
print(starts)
print(ends)

max_len = 0

for index in range(len(ends) - 1):
    diff = abs(ends[index] - starts[index + 1])
    if diff == 1:
        # join two sections together
        if index == 0:
            s_len = ends[index + 1] - starts[index + 1] + 1
        elif index == (len(days) - 1):
            s_len = ends[index] - starts[index] + 1
        else:
            s_len = (ends[index + 1] - starts[index + 1]) + (ends[index] - starts[index]) + 1
        if s_len > max_len:
            max_len = s_len
    else:
        # add one to the sections beside it
        if index == 0:
            s_len = ends[index + 1] - starts[index + 1] + 1
        elif index == (len(days) - 1):
            s_len = ends[index] - starts[index] + 1
        else:
            s_len_1 = ends[index] - starts[index] + 1
            s_len_2 = ends[index + 1] - starts[index + 1] + 1
            if s_len_1 > s_len_2:
                s_len = s_len_1
            else:
                s_len = s_len_2
        if s_len > max_len:
            max_len = s_len

print(max_len)