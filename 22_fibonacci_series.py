# # num=int(input("Enter any number :- "))
# # n1,n2=0,1
# # sum=0

# # if num <= 0:
# #     print("Please enter no greater then 0 :- ")
# # else:
# #     for i in range(0,num):
# #         print(sum,end="\n")
# #         n1 = n2
# #         n2 = sum        
# #         sum = n1 + n2  

num=int(input("Enter any number :- "))

n1=0
n2=1
sum=0

if num <= 0:
    print("Enter greater then 0 ")

else:
    for i in range(0,num):
        print(sum,end=" ")
        n1 = n2
        n2 = sum
        sum = n1 + n2


