

                   #METHOD OVERLODING
                   
class Human:
    def SayHello(self,Name = None):
        if Name!=None:
            print('Hello' + Name)
        else:
            print('Hello')
obj1=Human()
obj1.SayHello()
obj1.SayHello(' Shukla')