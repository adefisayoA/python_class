import sys
# import calculator
# A namespace is a collection of names, such as variable names,
# function names, and class names. Every Python module has its own namespace.
# <module>.<name>
from example_package import calculator as cal

# value = calculator.add(7, 2,5)
# print(f"The sum is {value}")
#
# value = calculator.subtract(5, 2)
# print(f"The difference is {value}")
# #
# # import calculator as cal - change the name of the module
# # import <module> as <other_name>
# # from <module> import <name>, <name> ... n

from calculator import divide, square
value = divide(5, 2)
print(f"The division is {value}")
#
# value = calculator.square(5, 2)
# print(f"The square is {value}")
#
# value = calculator.square_root(5)
# print(f"The square root is {value}")
