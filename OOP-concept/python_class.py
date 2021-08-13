class Dog:
    # class attribute
    species = "animal"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age


# instantiate the Dog class i.e create objects
A = Dog("Blu", -1)
B = Dog("Woo", 15)

# access the class attributes
print("A is a {}".format(A.__class__.species))
print("B is also a {}".format(B.__class__.species))

# access the instance attributes
print("{} is {} years old".format(A.name, A.age))
print("{} is {} years old".format(B.name, B.age))