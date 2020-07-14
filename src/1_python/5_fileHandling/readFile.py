# open file
file = open("test.txt")

# read file
# print("reading complete file")
# print(file.read())

# print("reading n char from complete file")
# print(file.read(12))

# read a line
# print(file.readline())

# print line by line using readLine method
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# print using readLines
lines = file.readlines()
for line in lines:
    print(line)

# close file
file.close()
