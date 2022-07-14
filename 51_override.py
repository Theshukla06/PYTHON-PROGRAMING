class A:
    def Display(self):
        print("This is my 1st price")
class B(A):
    def Display(self):
        print("This is my 2nd price")
class C(A):
    def Display(self):
        print("This is my all price")
        super().Display()
class D(B,C):
    def Display(self):
        print("This is my 4th price")
        super().Display()
obj = D()
obj.Display()