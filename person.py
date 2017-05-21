class Person:

    FORMAT_ATTR = "%-10s"
    FORMAT_VALUE = "%20s"
    FORMAT_ALL = FORMAT_ATTR + ": " + FORMAT_VALUE

    total_count = 0

    def __init__(self, name, email="", phone_number=""):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        Person.total_count += 1
        self.id = Person.total_count

    def print_info(self):
        print()
        print("----------------------------")
        print((Person.FORMAT_ALL) % ("ID", self.id))
        print((Person.FORMAT_ALL) % ("Name", self.name))
        print(("Email: " + Person.FORMAT_ATTR) % self.email)
        print(("Phone number: " + Person.FORMAT_ATTR) % self.phone_number)
