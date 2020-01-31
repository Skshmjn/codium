row = int(input("Enter the number of rows:"))


# For printing upper half of diamond
def upper_triangle(rows):
    k = 0
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(end=" ")

        while k != (2 * i - 1):
            print("*", end="")
            k = k + 1
        k = 0
        print()


# For printing bottom half of diamaond
def bottom_triangle(rows, k):
    m = 1
    for i in range(rows):
        for j in range(1, k):
            print(end=" ")
        k = k + 1

        while m <= (2 * (rows - i) - 1):
            print("*", end="")
            m = m + 1
        m = 1
        print()


if row % 2 is not 0:
    upper_triangle(row // 2 + 1)
    bottom_triangle(row // 2, 2)
else:
    upper_triangle(row // 2)
    bottom_triangle(row // 2, 1)
