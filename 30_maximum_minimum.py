# # a=10
# # b=9
# # maximum=max(a,b)
# # print(maximum)

# a=2
# b=3
# print(a if a >= b else b)

def maximum(a,b):
    if a >= b:
        return a
    else:
        return b

x=2
y=3

print(maximum(x,y))