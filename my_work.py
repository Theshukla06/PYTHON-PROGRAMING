# # # # # # # a=int(input('enter a'))
# # # # # # # b=int(input('enter b'))
# # # # # # # sum=a+b
# # # # # # # print(sum)

# # # # # # def sum(a,b):
# # # # # #     return a+b

# # # # # # a=int(input('enter a'))
# # # # # # b=int(input('enter b'))

# # # # # # a1=sum 
# # # # # # print(a1)

# # # # # n=int(input("enter number"))
# # # # # for i in range(1,11):
# # # # #     print(n,"X",i,"=",n*i)
    
# # # # #     # table=n*i
# # # # #     # print("*"i="table")
# # # # num = int(input("Enetr a no :-"))
# # # # if num % 2 == 0:
# # # #     print('prime no')

# # # # else:
# # # #     print('not prime no')

# # # # a="Shukla"
# # # # print(type(a))
# # # # n=int(a)
# # # # print(type(n))

# # # # for i in range (1,10+1):
# # # #     print(i)

# # # # x='2'

# # # # print(x)
# # # # x=int(x)
# # # # print(type(x))

# # # # #BOOLEAN
# # # # a= 5
# # # # b= 10
# # # # c= a<b
# # # # print(c)
# # # def Sum(a,b):
# # #     print('value A is :-',a)
# # #     print('value B is :-',b)
# # #     return a + b

# # # x= int(input("Enter A Value :- "))
# # # y= int(input("Enter B Value :- "))
# # # s=Sum(x,y)
# # # print(s)

# # #EVEN OR ODD NO PROGRAM
# # def Even_Odd(a):
# #     if a%2==0:
# #         print("Your no is Even :-",a)
# #     else:
# #         print("Your no is Odd :-",a)
# # x=int(input('Enter Value A :-'))
# # y=Even_Odd(x)

# # def Factorial(n):
# #     fact = 1
# #     for i in range(1,n+1):
# #         fact = fact * i
# #         return fact
# # a=int(input('Enter a :- '))
# # b=Factorial(a)
# # print('Your Factorial Ans is :-',b)

# from unicodedata import name


# class Student:
#     def setdata(self):
#         self.name=input('Enter Your Name :-')
#         self.age=int(input('Enter Your Age :-'))
#         self.colour=input('Enter Your Color :-')
#     def display(self):
#         print('Name :- ',self.name)
#         print('Age :- ',self.age)
#         print('Colour :- ',self.colour)
# a=Student()
# a.setdata()
# a.display()

l=[1,'x',22,'a']
print(l)
l1=[x for x in l if type(x)==int]
print(l1)

l2=[x for x in l if type(x)==str]
print(l2)