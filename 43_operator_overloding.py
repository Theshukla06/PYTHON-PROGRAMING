class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,b):
        return self.a+b.a
ob1=A(5)
ob2=A(5)
ob3=A("Ankit")
ob4=A("Shukla")

print(ob1+ob2)
print(ob3+ob4)