#Greatest of 3 no including equal

#Declaring variable and taking input

number1=float(input("Enter 1st no: "))
number2=float(input("Enter 2nd no: "))
number3=float(input("Enter 3rd no: "))

if number1>number2:
    if number1>number3:
        print(f"{number1} is largest")
    if number1==number3:
        print(f"{number1} and {number3} is largest")
    if number1<number3:
        print(f"{number3} is largest")
elif number1==number2:
    if number1>number3:
        print(f"{number1} {number2} is largest")
    if number1==number3:
        print(f"{number1} {number2} and {number3} is largest")
    if number1<number3:
        print(f"{number3} is largest")
if number1<number2:
    if number2>number3:
        print(f"{number2} is largest")
    if number2==number3:
        print(f"{number2} and {number3} is largest")
    if number2<number3:
        print(f"{number3} is largest")
