class A:
    def ShowDataA(self):
        print('I am in A ')
class B(A):    
    def ShowData(self):
        print('I am in B ')

obj=B()
obj.ShowDataA()
obj.ShowData()