import utils


# utils.print_table([[1, 2, 3], [4, 5, 6]])

#------------------------------------------------
# class type, id
# import student
    # def print_papers(self):
    #     for idx, paper in enumerate(self.papers):
    #         print("Paper %d: %s" % (idx, paper))

    # def print_info_ua(self):
    #     print("Имя: ", self.name)
    #     print("Курс: ", self.year)
    #     print("Возраст: ", self.age)

# student = Student()
# student2 = Student()

# student1 = student.Student("Alice", "MB", 19, 1)
# student2 = student.Student("Alice", "MB", 19, 1)
# print(type(student))

# print(id(student))
# print(id(student2))

# student.name = "Alice"
# student2.name = "Bob"

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


# student1.print_info()
# student2.print_info("UA")

import course
import professor
import student

if __name__ == "__main__":

    pr1 = professor.Professor("Dr. Adams")
    pr2 = professor.Professor("Dr. Smith")
    course1 = course.Course("ML")
    course2 = course.Course("MLX")

    course1.add_lecturer(pr1)
    course1.add_lecturer(pr2)
    # course1.print_info()

    pr1.add_course(course1)
    pr1.add_course(course2)

    pr1.print_info()

    st1 = student.Student("Alice", car="MB", age=17, year=2)
    st2 = student.Student("Bob")
    st1.print_info()
    # st2.print_info()


