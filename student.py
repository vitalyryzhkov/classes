import person

class Student(person.Person):
    # name = ""
    # age = 18
    # year = 1
    # papers = []
    # car = ""
    # achievements = None  # if there is nothing reaasonable

    def __init__(self, name, car="BMW", age=18, year=1):
        person.Person.__init__(self, name)
        # print("new student")
        # self.name = name
        self.age = age
        self.year = year
        self.car = car

    # @staticmethod
    def print_info(self, lang="EN"):
        #
        # i18n = {
        #     "EN": ["Name: ", "Year: ", "Age: ", "Car:"],
        #     "UA": ["Имя: ", "Год: ", "Возраст: ", "Авто:"]
        # }
        # return i18n

        # if lang == "EN":
        #     print("Name: ", self.name)
        #     print("Year: ", self.year)
        #     print("Age: ", self.age)
        #     print("Car:", self.car)
        # elif lang == "UA":
        #     print("Имя: ", self.name)
        #     print("Курс: ", self.year)
        #     print("Возраст: ", self.age)
        #     print("Авто:", self.car)
        person.Person.print_info(self)
        print("Age: %s" % self.age)
        print("Year: %s" % self.year)
        print("Car: %s" % self.car)

    def print_papers(self):
        for idx, paper in enumerate(self.papers):
            print("Paper %d: %s" % (idx, paper))



