# def function_name(argument1, ):
#     instruction

# create a function for division of two numbers
# create a function to subtract two numbers

def subtract_numbers(a,b):
    return a - b

x = subtract_numbers(6,4)
print(x)
#
# def add_numbers1(a,b,c):
#     return a + b + c
#
# print(add_numbers1(1,2))

# function parameter
def add_numbers(*args):
    result = 0
    for x in args:
        result += x # result +
    return result

print(add_numbers(1,2,3))

# # * Kwargs
# def add_shopping_list(**kwargs):
#     result = 0
#     for x in kwargs:
#         result += kwargs[x] # result +
#     return result

# print(add_shopping_list(egg =3, indomine = 5, bread =2))

# def add_ingrideint (*args, **kwargs):
#     result = 0
#     for arg in args:
#         result += arg
#     for key in kwargs:
#         result += kwargs[key]
#     return result
# print(add_ingrideint(1,2,3,egg =3, indomine = 5, bread =2 ))

