# from unicodedata import name


# rec={}
# n = int(input("Enter total no of stud :- "))
# i = 1
# while i <= n:
#     name = input("Enter Student name :- ")
#     marks = input("Enter % of Marks of stud :- ")
#     rec[name]=marks
#     i=i+1
# print("Enter of student "," \t ","% of marks")
# for x in rec:
#     print("\t",x,"\t\t",rec[x])

d={}
n=int(input('Number Of Element :- '))

for i in range(n):
    key=input('Enter key :- ')
    Name=input('Enter Name :- ')
    d.update({key:Name})
print(d)