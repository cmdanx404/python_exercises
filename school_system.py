class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def display(self):
        print(f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display(self):
        print(f"Teacher: {self.name}, Age: {self.age}, Subject: {self.subject}")

def school_system():
    student = Student("Alice", 14, 9)
    teacher = Teacher("Mr. John", 40, "Math")

    student.display()
    teacher.display()

school_system()
