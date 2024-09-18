# for loop which random number between 1-100, 10 times
#print the biggest number and the smallest number
import random

max_num: int = -1
min_num: int = 101
for _ in range(1, 10 +1):
    rand_int: int = random.randint(1, 100)
    print(rand_int, end = " ")
    if rand_int > max_num:
        max_num = rand_int
    if rand_int < min_num:
        min_num = rand_int
print(f"min number: {min_num}, max number: {max_num}")