# # def fib(n):
# #     if (n==1):
# #         return 0
# #     elif (n==2):
# #         return 1
# #     else:
# #         return(fib(n-1)+fib(n-2))
# # n=int(input('Enter n :- '))
# # for i in range(1,n+1):
# #     print(fib(i))


# def fibonacci(n):
#     if (n==1):
#         return 0
#     elif (n==2):
#         return 1
#     else:
#         return (fibonacci(n-1)+fibonacci(n-2))
# n=int(input('Enter value of n :-'))
# for i in range (1,n+1):
#     print(fibonacci(i))


import re


def febi(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return (febi(n-1)+febi(n-2))
n=int(input('Enter value n :- '))
for i in range (1,n+1):
    print(febi(i))
