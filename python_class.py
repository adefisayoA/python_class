# creating a class and why we need to use a class ####################################################
class Dog:
    pass


dog1 = Dog()
dog2 = Dog()

dog1.name = "Jack"
dog1.age = "3"

dog2.name = "Rex"
dog2.age = "5"

print(f"This is a dog: {dog1.name}, {dog1.age}")
print(f"This is a dog: {dog2.name}, {dog2.age}")

print("{} {}".format(dog1.name, dog1.age))

########################################################################################################
# # class Dog:
# #     # a function inside a class is called a method
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #     def __str__(self):
# #         return f"This is my dog; {self.name},{self.age} "
# #
# # buddy = Dog("Buddy", 9)
# # bingo = Dog("Bingo", 19)
#
# class Dog:
#     # a function inside a class is called a method
#     def __init__(self, name ="bingo", age=10):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"This is my dog; {self.name},{self.age} "
# #
# # my_dog = Dog()
# # print(my_dog)

########################################################################################################
# # create a new class for reproducing voters card - name, age, sex, soo ( state of origin )
# # instantiate the class to reproduce 5 voters card
# class Voters:
#     # a function inside a class is called a method
#     def __init__(self, name="Buhari", age=2, sex="F",soo="Abuja"):
#         self.__name = name
#         self.age = age
#         self.sex = sex
#         self.__soo = soo # make it private
#
#     def print_details(self):
#         print(f"This is the voter card for; {self.name},{self.age},{self.sex},{self.soo} ")
#     def __str__(self):
#         return f"This is the voter card for; {self.name},{self.age},{self.sex},{self.soo} "
# #
# votters = Voters()
# print(Voters.sex)
#
# imaobong = Voters("Joy",-20,"Female","Akwa-Ibom")
# folake = Voters("Folake",25,"Female","Oyo")
# chikezie = Voters("chikezie",24,"Female","Abia")
#
# imaobong.print_details();
# folake.print_details();
# chikezie.print_details();
#
#
# print(folake)
# def __str__(self):
#     return f"This is my dog; {self.name},{self.age} "
########################################################################################################
# # getters and setters
# class Animal:
#     def __init__(self, name="Rex", age=2):
#         self.__name = name
#         self.__age = age
#
#     def set_age(self, age):
#         if age > 0:
#             self.__age = age
#         else:
#             print("Age must be grater than 0.")
#
#     def get_age(self):
#         return self.__age
#
# def __str__(self):
#     return f"This is my dog {self.name},{self.age} "
#
# my_dog = Animal()
# my_dog.set_age(4)
# print(my_dog.get_age())


# print(my_dog)

########################################################################################################
# inheritance
# super class
#
# class Human:
#     def __init__(self, name, height, age):
#         self.name = name
#         self.height = height
#         self.age = age
#
#
# # child class
# class Programmer(Human):
#     def __init__(self, name, height, age, languages):
#         # super(Programmer, self).__init__(name, height, age)
#         super().__init__(name, height, age)
#         self.languages = languages
#
#
# xo = Programmer("James", 100, 25, "Python")
#
# # bob = Programmer("Bob", 180, 100, ["Python", "Java"])
#
# print(xo.name)  # Access to the name field inherited from the Human class
