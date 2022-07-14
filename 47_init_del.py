# #24. Write a program to use  __init__ and __del__ method.

# class Student:
#     def __init__(self):
#        print('The Object Is created')
    
#     def display(self):
#         print('Hello Ankit Shukla')
    
#     def __del__(self):
#         print("Object Is Deleted")
# s=Student()
# s.display()
# del(s)


class A:
    def __init__(self):
        print('Object Is Created')
    def display(self):
        print('Hy I Am Ankit Shukla')
    def __del__(self):
        print('Object Is Deleted')
a=A()
a.display()
del(a)