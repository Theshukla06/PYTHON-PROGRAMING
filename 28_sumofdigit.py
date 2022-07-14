from unittest import result


def Sumofdigit(n):
    if n==0:
        return 0
    return(n % 10 + Sumofdigit(int (n / 10)))
num = int(input("Enter Sum Of Digit Of Any Number :- "))
result=Sumofdigit(num)
print("Sum of digit in",num,"is",result)