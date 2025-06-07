# Exception Handling in Python
# Exceptions are errors that occur during the execution of a program. Python provides a way to handle these errors using try and except blocks.

try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code to handle the exception
    print("Error: Division by zero is not allowed.")
except Exception as e:
    # Catch any other exception
    print(f"An unexpected error occurred: {e}")
else:
    print("No errors!")
finally:
    # Code that will always execute, regardless of whether an exception occurred
    print("Execution completed.")
# x = 2
# try:
#     print(x/1)
# except NameError:
#     print("An error occurred.")
