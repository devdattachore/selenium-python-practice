# read a file and
# reverse its contents and
# write reversed contents in file

with open("test.txt", "r") as reader:
    lines = reader.readlines()
    print(lines)
    with open("test.txt", "w") as writer:
        reversedLines = reversed(lines)
        print(reversedLines)
        for line in reversedLines:
            writer.write(line)
