def function(a):
    if a % 2 == 0:
        return True
    else:
        return False
    
a=int(input("ENTER A :- "))
sol=function(a)

if sol == True:
    print("Number ",a,"is even")
else:
    print("Number",a,"is odd")


#a=int(input("Enter a 1st number :- "))
#if a%2==0:
#    print("Your number is even")
#else:
#    print("Your number is odd")