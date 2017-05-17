import utils


# utils.print_table([[1, 2, 3], [4, 5, 6]])

#------------------------------------------------
# class type, id
import student
    # def print_papers(self):
    #     for idx, paper in enumerate(self.papers):
    #         print("Paper %d: %s" % (idx, paper))

    # def print_info_ua(self):
    #     print("Имя: ", self.name)
    #     print("Курс: ", self.year)
    #     print("Возраст: ", self.age)

# student = Student()
# student2 = Student()

student = student.Student("Alice", "MB", 19, 1)
student2 = student.Student("Bob", "BMW", 22, 3)

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

