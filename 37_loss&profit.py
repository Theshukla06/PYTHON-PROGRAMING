c=int(input("Enter a cost price :-"))
s=int(input("Enter a selling price :-"))

if (c-s):
    loss = c - s
    print("Loss :- ",loss)
else:
    profit = s - c
    print("Loss :- ",profit)