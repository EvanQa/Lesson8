#print all numbers between range of 1-25 that do not divide by 7

for i in range(1, 25 + 1):
    if i % 7 != 0:
        print(i)

for i in range(1, 25 + 1):
    if i % 7 == 0:
        continue
    print(i)