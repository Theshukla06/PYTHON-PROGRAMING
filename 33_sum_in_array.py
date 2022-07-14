# # def Sum (arr):
# #     sum = 0
# #     for i in arr:
# #         sum = sum + i
# #     return(sum)
# # arr = []
# # arr = [10,10,10,10,10]
# # n = len(arr)
# # ans = Sum(arr)
# # print('Sum of the array is',ans)


# # arr = [10,10,10,10,10]
# # ans = sum(arr)
# # print('Sum of the array is',ans)

# lst = []
# n = int(input("Enter Number Of Elements :- "))
# for i in range(0,n):
#     ele = int(input())
#     lst.append(ele)
# print(lst)

arr = [10,10,10,10,10]
sum = 0

for i in range(0,len(arr)):
    sum = sum + arr[i]
print("Sum "+str(sum))

