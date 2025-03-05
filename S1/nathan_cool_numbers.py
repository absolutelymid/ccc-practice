num1 = int(input())
num2 = int(input())
count = 0
for i in range(num1, num2+1):
    if i ** 0.5 % 1 == 0:
        a = i ** (1/3)
        if a % 1 == 0:
            count += 1
print(count)

import math
math.cbrt()