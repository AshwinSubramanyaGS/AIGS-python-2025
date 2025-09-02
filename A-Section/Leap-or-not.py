#Program to print if leap year or not

#Declaring year and taking input

year=int(input("Enter the year: "))

#Leap year logic
'''
if year%4==0 or(year%100==0 and year%400==0):
    print(f"The year {year} is leap year")
else:
    print(f"The year {year} is not a leap year")
'''
print(f"The year {year} is ","leap year"if year%4==0 or(year%100==0 and year%400==0)else "not a leap year")
