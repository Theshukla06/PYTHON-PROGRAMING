# # # # from struct import pack_into
# # # # from unicodedata import name


# # #               #KEY ARGUMENTS

# def Printinfo(name,age):
#     print("Name :- ",name)
#     print("Age :- ",age)

# a=input("Enter Your Name :- ")
# b=int(input("Enter Your Age :- "))
# Printinfo(age=b,name=a)
# #Printinfo(age=22,name="Ankit Shukla")

# # #               #DEFAULT ARGUMENTS

from unittest import result


def Take_Power(a,b=4):
    p=1
    for i in range(b):
        p=p*a
        return p
result=Take_Power(3)
print(result)

result1=Take_Power(4,3)
print(result1)





# # # from unicodedata import name


# # # def Show(name,age=22):
# # #   print("Name :- ",name)
# # #   print("Age :- ",age)
# # #                                   #AGE IS DEFAULT ARGUMENT
# # # Show(name="Ankit Shukla")
 


 
# #                  #POSITIONAL ARGUMENT

# # def Power(x,y):
# #   print("X :-",x)
# #   print("Y :-",y)
# #   z=(x**y)
# #   print(z)

# # Power(5,2)      #POSITION ARGUMENT USE

