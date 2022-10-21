class Teacher:
    print('hello mark')

teacher_math = Teacher()

class Student:
    print('hello teacher')
    def __init__(self):
        self.height = 175
        self.age = 14

student_mark = Student()
print(student_mark.height)
print(student_mark.age)