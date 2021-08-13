# Example - Person, Employee finance calculation ############################
#

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"


# inherit the Person class and use it inside the Employees class. we can use the super() to be able to use the
# instance variable or object from the Person class
# class Employee(Person):
#     def __init__(self, name, age, rate, num_of_hour):
#         Person.__init__(self, name, age)
#         self.rate = rate
#         self.num_of_hour = num_of_hour
#
#     def show_finance(self):
#         return self.rate * self.num_of_hour
#
#
# class Student(Person):
#     def __init__(self, name, age, scholarship):
#         Person.__init__(self, name, age)
#         self.scholarship = scholarship
#
#     def show_finance(self):
#         return self.scholarship
#
#
# def check_finance(obj):
#     print(obj.show_finance())
#
#
# new_employee = Employee("Ronaldo", 36, 40, 10)
# new_student = Student("Messi", 34, 1000)
#
# check_finance(new_employee)  # an instance of the Employee class
# check_finance(new_student)  # an instance of the Student class


# Area calculator with polymorphism #############################################################
# base class
class Shape:
    s_length = 3

    def calculate_area(self):
        return self.s_length * 4


class Square(Shape):
    side_length = 2

    def calculate_area(self):
        return self.side_length * 2


class Triangle(Shape):
    base_length = 4
    height = 3

    def calculate_area(self):
        return 0.5 * self.base_length * self.height


# This function accepts an input object, and will call that object's calculate_area() method.
# Note that the object type is not specified. It could be a Square, Triangle, or Shape object.

def get_area(input_obj):
    print(input_obj.calculate_area())


# Create one object of each class
shape_obj = Shape()
square_obj = Square()
triangle_obj = Triangle()

# Now pass each object, one at a time, to the get_area() function and see the result.
get_area(shape_obj)
get_area(square_obj)
get_area(triangle_obj)

# Area calculator without  polymorphism #############################################################
# class Shape:
#     def calculate_area(self):
#         pass
#
#
# class Square:
#     side_length = 2
#
#     def calculate_square_area(self):
#         return self.side_length ** 2
#
#
# class Triangle:
#     base_length = 4
#     height = 3
#
#
# def calculate_triangle_area(self):
#     return (0.5 * self.base_length) * self.height
#
#
# def get_area(input_obj):
#     # Notice the type checks that are now necessary here. These type checks
#     # could get very complicated for a more complex example, resulting in
#     # duplicate and difficult to maintain code.
#
#     if type(input_obj).__name__ == "Square":
#         area = input_obj.calculate_square_area()
#
#     elif type(input_obj).__name__ == "Triangle":
#         area = input_obj.calculate_triangle_area()
#     print(area)
#
#
# # Create one object of each class
# square_obj = Square()
# triangle_obj = Triangle()
#
# # Now pass each object, one at a time, to the get_area() function and see the result.
# get_area(square_obj)
# get_area(triangle_obj)
