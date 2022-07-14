print("List with mixed elements ")
l1=[1,"x",4,5.6,"z",9,"a",0,4]
print(l1)
print("List with only integer elements :- ")
l2=[x for x in l1 if type(x)==int]
l3=[x for x in l1 if type(x)==float]
l4=[x for x in l1 if type(x)==str]
print(l2)
print(l3)
print(l4)