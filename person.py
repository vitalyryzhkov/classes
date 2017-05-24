class Person:

    __FORMAT_ATTR = "%-10s"
    __FORMAT_DELIM = ":"
    __FORMAT_VALUE = "%20s"
    __FORMAT_ALL = __FORMAT_ATTR + __FORMAT_VALUE

    __total_count = 0

    def __init__(self, name, email="", phone_number=""):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        Person.__total_count += 1
        self.__id = Person.__total_count

    def _format_row(self, attr_name, attr_value):
        attr_name_delim = attr_name + Person.__FORMAT_DELIM
        return Person.__FORMAT_ALL % (attr_name_delim, attr_value)

    def print_info(self, lang="EN"):
        print()
        print("-----------------------------")
        print(self._format_row ("ID", self.__id))
        print(self._format_row ("Name", self.name))
        print(self._format_row ("Email", self.email))
        print(self._format_row ("Phone", self.phone_number))
