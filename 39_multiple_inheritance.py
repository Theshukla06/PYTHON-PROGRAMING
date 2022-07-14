class A:
    def displayA(Self):
        print("Hy i am Ankit Shukla A")
class B():
    def displayB(Self):
        print("Hy i am Ankit Shukla B")
class C(A,B):
    def displayC(Self):
        print("Hy i am Ankit Shukla B")

obj=C()
obj.displayA()
obj.displayB()
obj.displayC()