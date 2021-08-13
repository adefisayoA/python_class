# # Protected members By adding _ to the beginning of the field name, we suggest to other developers that this variable
# # can be updated only by the methods of the given object.
# class Animal:
#     def __init__(self, name="Bingo", age=3):
#         self._name = name
#         self._age = age
#
#
# my_dog = Animal()
# print(my_dog._name)  # It will give the value of the name field of the my_dog object

#
# Python program to demonstrate protected members
# Creating a base class
# class Base:
#     def __init__(self):
#         # Protected member
#         self._a = 2
#
#
# # Creating a derived class
# class Derived(Base):
#     def __init__(self):
#         # Calling constructor of Base class
#         Base.__init__(self)
#         print("Calling protected member of base class: ")
#         print(self._a)
#
#
# obj1 = Derived()
# obj2 = Base()
#
# # Calling protected member Outside class will result in AttributeError
# print(obj2.a)

#
#
# Private members ##############
# To protect the fields and make the attributes private ,
# you must use a double underscore __ before the object variable name.
# class Animal1:
#     def __init__(self, name="Jack", age=12):
#         self.__name = name
#         self.__age = age
#
#
# my_dog = Animal1()
# print(my_dog.__name)  # Python will throw an error !!!


# using setters and getters
class Animal3:
    def __init__(self, name="Rex", age=5):
        self.__name = name
        self.__age = age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be grater than 0.")

    def get_age(self):
        return self.__age


my_dog = Animal3()
my_dog.set_age(3)
print(my_dog.get_age())  # It will display the updated value of the __age field of the my_dog object

#
# using Properties to encapsulate fields in a more "Python" way.
# Properties can have getter, setter and deleter methods.
class Animal:
    def __init__(self, name, age):
        self.__name = name # can not be change.
        self.__age = age

    @property  # getter - get field value
    def age(self):
        return self.__age

    @age.setter  # setter - sets a new field value
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be greater than 0.")

    @age.deleter  # deleter - delete the field
    def age(self):
        del self.__age


my_dog = Animal("Dog", 15)
my_dog.age = 3  # Sets age - uses setter
print(my_dog.age)  # Reads age - uses a getter
del my_dog.age  # Deletes the field - uses a deletion
