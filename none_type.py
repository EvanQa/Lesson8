# while loop which inputs number from the user 1-100 until gor -999
#print the biggest number and the smallest number

max_num: int = None
min_num: int = None
num_count: int = 0
num: int = int(input("enter a num between 1 - 100: "))
while True:
    num: int = int(input("enter a num between 1 - 100: "))
    if num == -999:
        break
    if num < 1 or num > 100:
        print("not in range")
        continue
    num_count += 1
    if max_num == None or num > max_num:
        max_num = num
    if min_num == None or num < min_num:
        min_num = num
print(f"total numbers is: {num_count}")
print(f"min number: {min_num}")
print(f"max number: {max_num}")