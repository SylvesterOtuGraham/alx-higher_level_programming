#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastnum = abs(number) % 10
if number < 0:
    lastnum = -lastnum
print(f"Last digit of {number:d} is {lastnum:d} and is ", end="")
if lastnum > 5:
    print("greater than 5")
elif lastnum == 0:
    print("0")
else:
    print("less than 6 and not 0")
