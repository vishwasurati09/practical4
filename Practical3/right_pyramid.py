# Inverted Right Half Pyramid

rows = 6

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


num = 1
rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
        if num == 10:
            num = 1
    print()
