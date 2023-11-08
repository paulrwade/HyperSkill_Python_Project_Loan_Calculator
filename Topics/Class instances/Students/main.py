class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.student_id = name[0] + last_name + birth_year

    def get_id(self):
        print(self.name[0] + self.last_name + self.birth_year)


name = str(input())
last_name = str(input())
birth_year = str(input())

student_1 = Student(name, last_name, birth_year)

student_1.get_id()