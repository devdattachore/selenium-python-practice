obj = [1, 5, 6, 23, 565]

for each in obj:
    print(each)

summation = 0
for j in range(1, 6):
    print(j)
    summation = summation + j
print(summation)

# skip initial index (0 to 5)
for j in range(6):
    print(j)

# change incrementer to 3
for j in range(0, 14, 3):
    print(j)
