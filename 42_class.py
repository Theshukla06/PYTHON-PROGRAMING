class Student:
    def setdata(self):
        self.name=input("Enter your  name :- ")
        self.roll=int(input("Enter your roll no :- "))
        self.pers=float(input("Enter your Persentage :- "))
    def display(self):
        print("Your Name Is :",self.name)
        print("Your Roll no Is :",self.roll)
        print("Your Persentage Is :",self.pers)
a=Student()
a.setdata()
a.display()