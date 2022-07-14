#Program to implement the concept of method overloading.
class Person:
    def Hello(self , name = None):
        if name is not None:
            print('Hello'+name)
        else:
            print('Hello')
a=Person()
a.Hello()
a.Hello(' Ankit Shukla')