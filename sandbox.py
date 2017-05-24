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


b = B("AAA")
print("D.__init__")


class C(A):
    def __init__(self, name):
        super().__init__(name)
        # A.__init__(self, name)
        print("C.__init__")

    def methodB(self):
        pass



class D(B, C):
    def __init__(self, name):
        super().__init__("bbb")
        # B.__init__(self, "bvbb")
        # C.__init__(self, "ccvc")
        def methodB(self):
            print("methodB")


print(b.attr1)
print(b.name)
b.methodA()
b.methodB()

d = D("BBB")

print(d.name)
d.methodA()
print(d.attr1)
d.methodB()
