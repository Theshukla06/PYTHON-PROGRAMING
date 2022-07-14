#Write a program to solve quadratic equation ax2+bx+c=0

# import cmath

# a=int(input("Enter a :- "))
# b=int(input("Enter b :- "))
# c=int(input("Enter c :- "))

# d=(b**2)-(4 * a * c)

# sol1 = - b - cmath.sqrt(d)/(2*a)
# sol2 = - b + cmath.sqrt(d)/(2*a)

# print("Your Quadratic Equation Ans :- ",sol1)
# print("Your Quadratic Equation Ans :- ",sol2)

# import cmath


# a=int(input("Enter a :- "))
# b=int(input("Enter b :- "))
# c=int(input("Enter x :- "))

# d=(b**2)-(4*a*c)

# sol1 = - b - cmath.sqrt(d)/(2*a)
# sol2 = - b + cmath.sqrt(d)/(2*a)

# print ("YOUR QUADRATIC EQUATION :- ",sol1,sol2)



import cmath


a=int(input("Enter Value a :-"))
b=int(input("Enter Value b :-"))
c=int(input("Enter Value c :-"))

ans1=(-b + cmath.sqrt(b*b-4*a*c)) / (2*a)
ans2=(-b - cmath.sqrt(b*b-4*a*c)) / (2*a)

print("YOUR QUADRATIC EQUATION ANS IS :- ",ans1,ans2)