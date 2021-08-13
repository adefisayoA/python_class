# conditional statements (if, elif, else),
# loops (for, while).

# # # if statement
# # if <expr>:
# #     <statement> # one way logic
#   else:
#        <statement> # this is the option to take


# if x > y:
#     print(f"{x} is greater than {y}")
# else:
#     print(f"{x} is less than {y}")
#
# # rich man, good man, respactable man, ... Man

# #elif
# x = 5 # assignment operator ? x is a variable  = 5
# y = 15
# if x > y:
#     print(f"{x} is greater than {y}")
# elif x == 5:  # equality?
#     print(f"{x} is equal than {y}")
# else:
#     print(f"{x} is less than {y}")

# loops (for, while) - iteration  / loop

# while condition:
#     <instructions_1>
#     <instructions_2>

# n = 0 # initalize
# while n < 100: # while n is not greater than 10
#     n +=1
#     print(n)

# loop termination
# break statement - stop the loop / exit the loop block
# continue statement - stop the current iteration and continue with the next.

# n = 0 # initalize
# while n < 7: # while n is not greater than 10
#     n +=1 # increment n with each loop
#     if n == 6: # if n is 5, end the loop
#         break
#     # if n == 2: # if n is 1, start a new iteration
#     #     continue
#     print(n)
#
# for var in iterable:  # iterable is a collection of variables / value that you can iterate - list
#     instruction

# animals = ["dog", "cat", "Fish"] # iterable
#
# for animal in animals:
#     print(animal)

# range function
# range(start, stop, step) # range function starts from 0
# 0,1,2 - range(3)

# for i in range(3):
#     print(i)
#
# for i in range(3,11,2): # start - 3, stop - 11, take 2 steps
#     print(i)

# write a program to print out all even numbers between 2 to 20 using the range function
for i in range(2,20,2):
    print(f"the even number between 2 and 20 are: " + {i})

# enumerate function
# list and dictionary comprehension

