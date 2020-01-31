In the block finally will run irrespective of whether the block is executed successfully or not.

eg: it is use to close connection and files whether the desired output is obtained or not.

whereas else will run if the block it followed executed without any exception
eg;
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...