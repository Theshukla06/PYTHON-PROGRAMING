lower = int(input("Enter Lower number :- "))
upper = int(input("Enter Upper Number :- "))

for num in range (lower, upper + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i)==0:
                break
        else:
            print(num)