# #23. Program (Operator overloading)

# class A:
#     def __init__(self,a):
#         self.a=a
#     def __gt__(self,other):

#         if (self.a > other.a):
#             return True
#         else:
#             return False

# obj1=A(10) # <---- VALUE ---> 10
# obj2=A(20) ## <---- VALUE ---> 20   (10>20)
# if (obj1 > obj2):
#     print('Obj 1 Greator Then Obj 2')
# else:
#     print('Obj 2 Greator Then Obj 1')

class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return self.a + other.a
obj1=A(10)
obj2=A(20)
obj3=A('Ankit')
obj4=A('Shukla')

print(obj1+obj2)
print(obj3+obj4)