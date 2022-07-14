# # from math import factorial


# # num=int(input("Enter a number :- "))
# # factorial=1
# # if num <= 0:
# #     print("Enter greator then 0 ")
# # else:
# #     for i in range(1,num+1):
# #         factorial=factorial*i
# #         print("Factorial :- ",num,factorial)



# # num=int(input("Enter a number :- "))
# # factorial=1
# # # if num <= 0:
# # #     print("Enter greator then 0 ")
# # # else:
# # for i in range(1,num+1):
# #    factorial=factorial*i
# #    print("Factorial :- ",factorial)

# a=int(input ("Enter a number :- "))
# fact=1
# while(a > 0):
#   fact=fact * a
#   a = a - 1
# print("Factorial :- ",fact)

def Fact(a):
  if a==1:
    return 1
  return a * Fact (a - 1)

a = int(input("Enter a number :- "))
f1 = Fact(a)
print("Factorial :- ",f1)

