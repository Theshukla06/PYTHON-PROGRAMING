# def module(a):
#     #print("a = ",a)
#     return a*a

# n=int(input("Enter a number :-"))
# val=module(n)
# print("Value = ",val)

# def module(a,b):
#     # print("a = ",a)
#     # print("b = ",a)
#      return a+b , a*b

# a=int(input("Enter a number :-"))
# b=int(input("Enter a number :-"))
# val1=module(a,b)

# print("Value = ",val1)


from msilib.schema import tables


def Table(num):
     for i in range (1,11):
         print(num,"X",i,"=",num*i)

num=int(input("Enter a number :-"))
Table(num)
