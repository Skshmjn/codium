num = int(input("Enter the number :"))

for i in range(num):
    if i > 1:
        for n in range(2, i):
            if (i % n) == 0:
                break
        else:
            print(i, end=" ")
