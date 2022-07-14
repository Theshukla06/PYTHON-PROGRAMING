def Printinfo(*v):
    sum=0
    for i in v:
        sum=sum+i
    return sum
s=Printinfo(10.5)
print(s)
s=Printinfo(70,60.2,50.4)
print(s)
s=Printinfo(1,10,90,68,76,45)
print(s)