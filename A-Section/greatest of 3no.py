#Greatest of 3 number

#Declaring variable and taking input

num_1=float(input("enter number1: "))
num_3=float(input("enter number3:"))
num_2=float(input("enter number2:"))

#Print Greatest of 3 no
if num_1>=num_2 and num_1>=num_3:
    print(f"{num_1} is largest of 3")
elif num_2>=num_3 and num_2>=num_1:
    print(f"{num_2} is largest of 3")
else:
    print(f"{num_3} is largest of 3")
    
