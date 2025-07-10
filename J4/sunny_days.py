# CCC 25' J4
x = int(input())
days = ''.join([input() for _ in range(x)])
# print(days)

day_blocks = []
prev_day = ''
block = ''
for day in days:
    if not prev_day:
        prev_day = day
        block += day
    else:
        if prev_day == day:
            block += day
        else:
            day_blocks.append(block)
            block = ''
            block += day
            prev_day = day

# print(day_blocks)

s_length = 0

# strat
# if there are periods with only one rainy day, see if they can be used to join two sectiosn together
# else, tack a one onto the longest sunny period


for block in range(len(day_blocks)):
    # single period of rain
    if len(day_blocks) == 1:
        # only a single day/period of rain
        if 'P' in day_blocks[block]:
            s_length = 1
        # only a single day/period of sun
        else:
            # multiple sunny days (periods)
            if len(day_blocks[block]) > 1:
                s_length = len(day_blocks[block]) - 1
            # single sunny day
            else:
                s_length = 0
    # more than one period of weather
    else:
        # check only days with precipitation
        if 'P' in day_blocks[block]:
            # if precipitation period is only a day long
            if len(day_blocks[block]) == 1:
                # check length of sunshine periods surrounding it
                # if day is at the end of the data
                if (len(day_blocks) - 1) == block:
                    new_s_length = len(day_blocks[block - 1]) + 1
                    if new_s_length > s_length:
                        s_length = new_s_length
                # if day is at beginning of data
                elif 0 == block:
                    new_s_length = len(day_blocks[block + 1]) + 1
                    if new_s_length > s_length:
                        s_length = new_s_length
                # normal case: sandwiched in between
                else: 
                    new_s_length = len(day_blocks[block - 1]) + len(day_blocks[block + 1]) + 1
                    if new_s_length > s_length:
                        s_length = new_s_length
            else:
                # check length of nearby S blocks
                # if day is at the end of the data
                if (len(day_blocks) - 1) == block:
                    new_s_length = len(day_blocks[block - 1]) + 1
                    if new_s_length > s_length:
                        s_length = new_s_length
                # if day is at beginning of data
                elif 0 == block:
                    new_s_length = len(day_blocks[block + 1]) + 1
                    if new_s_length > s_length:
                        s_length = new_s_length
                # normal case: sandwiched in between
                else:
                    # check left side
                    new_s_length = len(day_blocks[block - 1]) + 1
                    if new_s_length > s_length:
                        s_length = new_s_length
                    # check right side
                    new_s_length = len(day_blocks[block + 1]) + 1
                    if new_s_length > s_length:
                        s_length = new_s_length

print(s_length)