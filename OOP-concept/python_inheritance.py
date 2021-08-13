class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"


# inherit the Person class and use it inside the Employees class. we can use the super() to be able to use the
# instance variable or object from the Person class
class Employee(Person):
    def __init__(self, name, age, rate, num_of_hours):
        super().__init__(name, age)
        self.rate = rate
        self.num_of_hours = num_of_hours

    def show_finance(self):
        return self.rate * self.num_of_hours


class Student(Person):
    def __init__(self, name, age, scholarship):
        super().__init__(name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship


new_person = Person("Mbape", 20)
new_employee = Employee("Ronaldo", 36, 40, 1800)
new_student = Student("Messi", 34, 1000)
print(new_person)
print(new_employee)
print(new_student)
