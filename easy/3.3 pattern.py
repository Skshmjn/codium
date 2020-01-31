row = int(input("Enter the number of rows:"))

k = 0
for i in range(0, row):

    for j in range(k, row - 1):
        print(' ', end='')

    print("*", end='')

    for j in range(k * 2 - 1):
        print(' ', end='')
    if i is not 0:
        print("*", end="")
    print()
    k += 1
