p=10000
r=10.25
t=5

Amount = p * (pow((1+ r / 100),t))
CI = Amount - p
print("Compond Interest :- ",CI)