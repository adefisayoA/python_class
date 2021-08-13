class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"


# inherit the Person class and use it inside the Employees class. we can use the super() to be able to use the
# instance variable or object from the Person class
class Employee(Person):
    def __init__(self, name, age, rate, num_of_hour):
        Person.__init__(self, name, age)
        self.rate = rate
        self.num_of_hour = num_of_hour

    def show_finance(self):
        return self.rate * self.num_of_hour


class Student(Person):
    def __init__(self, name, age, scholarship):
        Person.__init__(self, name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship


# student who both has a scholarship and is paid for the hours he worked

class WorkingStudent(Employee, Student):
    def __init__(self, name, age, rate, num_of_hour, scholarship):
        Employee.__init__(self, name, age, rate, num_of_hour)
        Student.__init__(self, name, age, scholarship)

    def show_finance(self):
        return self.rate * self.num_of_hour + self.scholarship

    def __str__(self):
        return f"{self.name} is {self.age} years old earning {self.scholarship}"


new_person = Person("Mbape", 20)
new_employee = Employee("Ronaldo", 36, 40, 10)
new_student = Student("Messi", 34, 1000)
new_workingStudent = WorkingStudent("Folusade", 45, 10.5, 120, 3800)

print(new_person)
print(new_employee)
print(new_student)
print(new_workingStudent)

# # Method Resolution Order (MRO)
print(WorkingStudent.mro())  # This will print list
print(WorkingStudent.__mro__)  # This will print tuple
