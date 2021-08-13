sentence = "Today is a good day"
sentence1 = "Thank God it is Friday"

# length of our string ?
#functions - implementation of some basic steps
# len() - total character inclusive of whitespace in our string
# x = len(sentence)
# print(x)
#
# y = len(sentence1)
# print(y)

# index() function - no that is equal to the position of first occurrence of a specified string
# z = sentence.index("g")
# print(z)

# .count() function - know of time a specified character occurs in the string
# print(sentence.count("y"))

# [] = list
# sentence = "Today is a good day"
# print(sentence[6])

# string slicing
# start index (inclusive), colon, and end index (exclusive - its not part of it )
print(sentence[0:5]) # the beginning
# day is
print(sentence[2:8])

# good day
print(sentence[11:])

# Today is a good
print(sentence[:15])

# steps slicing
# sentence = "Today is a good day" << ---
print(sentence[0:15:3])

# string reversal
print(sentence[:-2])

# upper() function
# sentence = "Today is a good day"
print(sentence.upper())
# lower() function
print(sentence.lower())

#write a pro









