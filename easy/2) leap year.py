# Taking input year
input_year = int(input("enter year:"))

# Leap Year Algorithm
if input_year % 4 is 0 and input_year % 100 is not 0:
    print(input_year, " -> ", True)
elif input_year % 100 is 0:
    print(input_year, " -> ", False)
elif input_year % 400 is 0:
    print(input_year, " -> ", True)
else:
    print(input_year, " -> ", False)
