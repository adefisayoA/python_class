import re

# #search
# print(re.search(r"[A-Z]la", "ala Ola Ela"))
#
# # match function
# print(re.match(r"[A-Z]la", "ala Ola Ela"))
#
# # fullmatch function
# print(re.fullmatch(r"[A-Z]la", "Ela"))
#
# # findall function
# print(re.findall(r".la", "Ola ala Ela"))


#split function
print(re.split(r",|\.", "apple,pear,grapes,carrot.cabbage,veggies.fruit,yard"))

# pattern = r"123"
# string = "123zzb"
# re.match(pattern, string)
#
# # Out: <_sre.SRE_Match object; span=(0, 3), match='123'>
# match = re.match(pattern, string)
# print(match.group())