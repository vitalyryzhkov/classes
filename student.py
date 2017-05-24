import person

#------------------------------------------------
# class type, id
class Student(person.Person):

    def __init__(self, name, age=18, year=1):
        person.Person.__init__(self, name)
        print("I'm new Student")
        # self.name = name
        self.age  = age
        self.year = year
        self.papers_local = []

    # @staticmethod
    def print_info(self, lang="EN"):
        # i18n = {
        #     "EN": ["Name", "Year", "Age"],
        #     "UA": ["Им'я", "Рiк",  "Вiк"],
        #     "IT": ["Name", "Year", "Age"],
        #     "FR": ["Name", "Year", "Age"],
        # }
        #
        # print(i18n[lang][0], ": ", self.name)
        # print(i18n[lang][1], ": ", self.year)
        # print(i18n[lang][2], ": ", self.age)
        person.Person.print_info(self)
        print(self._format_row ("Year", self.year))
        print(self._format_row ("Age", self.year))

    def print_papers(self):
        for idx, paper in enumerate(self.papers_local):
            print("Paper %d: %s" %(idx, paper))
