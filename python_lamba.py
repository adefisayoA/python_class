# def add(a,b):
#     return a + b
#
# print(add(4,6))
#
# add_expression = lambda a,b: a + b
# square_expression = lambda x: x ** 2
#
# print(add_expression(5,7))
# print(square_expression(5))

# # map reduce filter
# map(function,list|tuple|iterable object)
# # compute the square of a list of numbers
# list_no = [25,36,64]
# # result = map(lambda x: x ** 2, list_no)
# # print(list(result ))
#
# import math
# sqrt_no = map(math.sqrt, list_no)
# print(list(sqrt_no))
# #
# # # write lamba expression to compute division
# # def div(a,b):
# #     return a/b
#
# list_item = [1,2,3,4,5,6]
# result = map(lambda x: x ** 2, list_item)


list_item = [1,2,3,4,5,6]
result = filter(lambda x: x %2, list_item)
# filter(function, iterable )
print(list(result))

list_item = [1,2,3,4,5,6]
result = filter(lambda x: x > 3, list_item)
print(list(result))

# reduce