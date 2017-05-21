import person

class Professor(person.Person):
    def __init__(self, name):
        person.Person.__init__(self, name)
        # self.name = name
        self.courses = []

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def print_info(self):
        # print("Lecture: %s" % self.name)
        person.Person.print_info(self)
        print("Courses: ")
        for course in self.courses:
            print("\t%s" % course.name)
