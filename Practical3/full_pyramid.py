# Centered Full Pyramid (Triangle)

rows = 5

for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")

    # Print stars
    for k in range(i):
        print("* ", end="")

    print()
    # Full Pyramid Pattern with Letters

rows = 5  # Number of rows in the pyramid

for i in range(rows):
    # Print leading spaces
    print(" " * i, end="")
    
    # Print letters from A onwards, decreasing each row
    for j in range(rows - i):
        print(chr(65 + j), end=" ")
    
    print()  # Move to next line

