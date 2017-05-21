class A:
    def __init__(self, name):
        print("A.__init__")
        self.attr1 = "attrA"
        self.name = name

    def methodA(self):
        print("methodA")

class B(A):
    def methodB(self):
        print("methodB")


class D(B):
    def __init__(self, name):
        B.__init__(self, name)
        print("D.__init__")


b = B("AAA")


print(b.attr1)
print(b.name)
b.methodA()
b.methodB()

d = D("BBB")

print(d.name)
d.methodA()
print(d.attr1)
d.methodB()
