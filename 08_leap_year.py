year=int(input("Enter Any Year :-"))
if year % 4 == 0 and year % 100 != 0:
    print("Given Year Is Leap Year ")
elif year %100==0:
    print("Given year is not leap year")
elif year % 400 == 0:
    print("Given Year Is Leap Year ")
else:
    print("Given year is not leap year")