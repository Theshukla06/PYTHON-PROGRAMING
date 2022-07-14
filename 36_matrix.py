# num1 = ([1,2,3],[3,2,1],[4,5,6])
# num2 = ([1,2,3],[3,2,1],[4,5,6])


# for i in num1:
#     print(i)
# for j in num2:
#     print(j)

# num3 = num1+num2
# print(num3,end=" ") 

from unittest import result


X = [[1,2,3],[3,2,1],[4,5,6]]
Y = [[1,2,3],[3,2,1],[4,5,6]]


result = [[0,0,0],[0,0,0],[0,0,0]]
print(X)
print(Y)
for i in range(len(X)):
    for j in range(len(Y)):
        result[i][j] = X[i][j] + Y[i][j]
for r in result:
    print(r)