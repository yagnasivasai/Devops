class student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.msg = self.name + " got a grade " + self.grade


stud1 = student("nia", "b")
print(stud1.name)
print(stud1.msg)
print(stud1.grade)
