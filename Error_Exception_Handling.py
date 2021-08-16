# gives me ZeroDivisionError exception ####################################################
class customException(Exception):
    def __init__(self):
        message = "The number can not be divided by zero"
        super().__init__(message)


a = 5
b = [2, 6,  0]
for val in b:
    if val ==0:
        raise customException()
    answer = a / val
    print(f"Result is: {answer}")

# a = 4
# b = -7

#
# def mul(a, b):
#     if a < 0 or b < 0:
#         raise ValueError("The number must be positive number")
#     else:
#         print(a * b)
#
#
# mul(a, b)


# def area_square(side):
#     try:
#     areaS = side * 2
#     return areaS

# print(area_square(-4))

# using the Use try...except: to catch exceptions.##########################################
# a = 5
# b = [2, 0, 6]
# for val in b:
#     try:
#         answer = a / val
#     except ZeroDivisionError:
#         continue
#     print(f"Result is: {answer}")

########################################################################################################
# The exception class that is specified - in this case, ZeroDivisionError
# catches any exception that is of that class or of any subclass of that exception.
# a = 5
# b = [2, 0, 6]
# for val in b:
#     try:
#         answer = a / val
#     except ArithmeticError:
#         continue
#     print(f"Result is: {answer}")


###########################################################
# Exception - finally. The finally clause would regardless of whether the exception occurred or not.
# try:
#     x = 5 / 0
# except ZeroDivisionError as e:
#     # `e` is the exception object
#     print("Got a divide by zero! The exception was:", e)
#     # handle exceptional case
#     x = 0
# finally:
#     print("The END")
# # it runs no matter what execute.

###########################################################
# Re-raising exceptions
# a = 5
# b = [2, 0, 6]
# for val in b:
#     if val == 0:
#         raise ValueError("The divisor cannot be zero")
#         answer = a / val
#     result = a / val
#     print(f"Result is: {result}")


###########################################################
# def even_the_odds(odds):
#     if odds % 2 != 1:
#         raise ValueError("Did not get an odd number")
#     else:
#         print("even number")


# print(even_the_odds(7));
###########################################################
# For each try block, you can define multiple except blocks depending on how you want to handle errors of that type.
# try:
#         # the string of statements where the error may occur
#     except ValueError:
#         # handling an exception of type ValueError
#     except (ZeroDivisionError, KeyError):
#         # handling exceptions of the ZeroDivisionError and KeyError types
#     except:
#         # handling all other exceptions
