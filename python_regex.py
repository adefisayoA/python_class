import re

# #search#################################################
# print(re.search(r"[A-Z]la", "ala Ola Ela"))
#
# # match function #################################################
# print(re.match(r"[A-Z]la", "ala Ola Ela"))
iter = re.finditer(r".la", "Ola ala Ela")
for value in iter:
    print(value)

# x
# # fullmatch function #################################################
# print(re.fullmatch(r"[A-Z]la", "Ela"))
#
# # findall function #################################################
# print(re.findall(r".la", "Ola ala Ela"))
#
#
# #split function #################################################
# print(re.split(r",|\.", "apple,pear,grapes,carrot.cabbage,veggies.fruit,yard"))

# pattern = r"123"
# string = "123zzb"
# re.match(pattern, string)
#
# # Out: <_sre.SRE_Match object; span=(0, 3), match='123'>
# match = re.match(pattern, string)
# print(match.group())


############# use regex to confirm valid emial #########################
# import re

# folake234@gmail.uk| susan@yahoo.com | imabong@hotmail.ng
# # folake234@gmail.uk| susan@YAHOO.com | imabong@hotmail.ng
#
check_email = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|uk|net|ng)"
user_email = input("provide an email:")
if (re.search(check_email, user_email)):
        print("email syntax is correct")
else:
        print("email syntax is not correct")
