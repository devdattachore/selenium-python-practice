try:
    with open("test.txt", "r") as reader:
        print(reader.read())

except Exception as e:
    print("customized error message")  # OP: customized error message
    print(e)  # OP: [Errno 2] No such file or directory: 'test.txt'

finally:
    print("this block will be reached no matter if there is exception or not")

# O/P
# customized error message
# [Errno 2] No such file or directory: 'test.txt'
# this block will be reached no matter if there is exception or not
