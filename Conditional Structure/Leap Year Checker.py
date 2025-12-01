year = int(input("Enter a year: "))

# A leap year is divisible by 4, except for end-of-century years which must be divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is a leap year")
else:
    print("It is not a leap year")