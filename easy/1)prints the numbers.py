# Main function
for i in range(1, 101):
    if i % 5 is 0 and i % 3 is 0:
        print("FizzBuzz ", end=" ")
    elif i % 5 is 0:
        print("Buzz", end=" ")
    elif i % 3 is 0:
        print("Fizz", end=" ")
    else:
        print(i, end=' ')
    # For expected output as in assignment
    if 0 == i % 20:
        print("\n")
