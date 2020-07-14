values = [1, 2.3, "abc"]
print(values)
print(values[1])
print(values[2])
print(values[-1])  # -1 prints last index
values.insert(2, "def")  # insert item at specific index
print(values)
values.append("appended at last")  # insert item at last index
print(values)
values[1] = 3.4  # update item at an index
print(values)

