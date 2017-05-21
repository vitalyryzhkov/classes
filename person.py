class Person:

    FORMAT_ATTR = "%10s"
    FORMAT_VALUE = "%20s"
    FORMAT_ALL = FORMAT_ATTR + ": " + FORMAT_VALUE

    def __init__(self, name, email="", phone_number=""):
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def print_info(self):
        print()
        print("----------------------------")
        print((Person.FORMAT_ALL) % ("Name", self.name))
        print(("Email: " + Person.FORMAT_ATTR) % self.email)
        print(("Phone number: " + Person.FORMAT_ATTR) % self.phone_number)
