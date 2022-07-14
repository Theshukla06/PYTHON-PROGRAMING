class A:
    def displayA(self):
        print('Hy I"am in Class A')
class B:
    def displayB(self):
        print('Hy I"am in Class B')
class C (A,B):
    def displayC(self):
        print('Hy I"am in Class C')
a=C()
a.displayA()
a.displayB()
a.displayC()
