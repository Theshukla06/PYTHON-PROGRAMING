# a=3
# b=4
# c=5
# simple_interest = (a*b*c)/100
# print("Your Simple Interest value is :- ",simple_interest )

def Simple_interest (p,t,r):
    print('The principal is',p)
    print('The principal is',t)
    print('The principal is',r)
    si=(p*t*r)/100
    print('Simple_interest',si)
    return si

Simple_interest(8,6,8)