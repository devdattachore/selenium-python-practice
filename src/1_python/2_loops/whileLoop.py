limit = 10

while limit > 0:
    if limit == 6:
        limit = limit - 1
        print("skipping 6")
        continue
    if limit == 3:
        print("breaking after 3")
        break
    print(limit)
    limit = limit - 1
