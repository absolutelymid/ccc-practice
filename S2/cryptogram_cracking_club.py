# CCC '25 S2
cipher = input()
cipher_split = []
section = ''
prev_char = ''
for char in cipher:
    try: prev_char = int(prev_char)
    except: pass
    if ord(char) >= ord('a') and ord(char) <= ord('z') and type(prev_char) == int:
        cipher_split.append(section)
        section = ''
    section += char
    prev_char = char
cipher_split.append(section)

# find length of cipher and create dictionary
cipher_letter = []
cipher_count = []
length = 0
for section in cipher_split:
    section = list(section)
    letter = section.pop(0)
    section = int(''.join(section))
    length += section
    cipher_count.append(section)
    cipher_letter.append(letter)

# use c to find letter
c = int(input())
remain = c % length
for count in range(len(cipher_count)):
    remain -= cipher_count[count]
    if remain < 0:
        print(cipher_letter[count])
        break

# problematic test case:
# a4b1c2d10
# 17

# use c to find letter
# c = int(input())
# remain = c % length
# if c == length: remain = length
# for count in range(len(cipher_count)):
#     remain -= cipher_count[count]
#     if remain <= 0:
#         print(cipher_letter[count])
#         break