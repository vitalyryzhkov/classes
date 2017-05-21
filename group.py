class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, new_student):
        self.students.append(new_student)

    def print_info(self):
        print("Course title: %s" % self.name)
        print("Lecturers: ")
        for student in self.students:
            print("\t%s" % student.name)

