class Student:
    name = ""
    age = 18
    year = 1
    papers = []
    car = ""
    achievements = None  # if there is nothing reaasonable

    def __init__(self, name, car, age=18, year=1):
        print("new student")
        self.name = name
        self.age = age
        self.year = year
        self.car = car

    # @staticmethod
    def print_info(self, lang="EN"):
        if lang == "EN":
            print("Name: ", self.name)
            print("Year: ", self.year)
            print("Age: ", self.age)
            print("Car:", self.car)
        elif lang == "UA":
            print("Имя: ", self.name)
            print("Курс: ", self.year)
            print("Возраст: ", self.age)
            print("Авто:", self.car)

    # def print_papers(self):
    #     for idx, paper in enumerate(self.papers):
    #         print("Paper %d: %s" % (idx, paper))

    # def print_info_ua(self):
    #     print("Имя: ", self.name)
    #     print("Курс: ", self.year)
    #     print("Возраст: ", self.age)

# student = Student()
# student2 = Student()

student = Student("Alice", "MB", 19, 1)
student2 = Student("Bob", "BMW", 22, 3)

# print(type(student))

# print(id(student))
# print(id(student2))

student.name = "Alice"
student2.name = "Bob"

# print(student.name)
# print(student2.name)

# Student.print_info(student)
# Student.print_info(student2)

# student.print_info()
# student2.print_info()

# student.papers.append("Math")
# student2.papers.append("Literature")
# student.print_papers()
# student2.print_papers()


student.print_info()
student2.print_info("UA")
