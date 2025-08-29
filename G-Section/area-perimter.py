'''Write a Python program to calculate the area
and perimeter of a rectangle using variables and operators.'''

#Declaring and taking input of length and bredth

length=float(input("Lenth of rectangle: "))
bredth=float(input("Bredth of rectangle: "))

#Calculating Area and perimeter of recange

area=length*bredth

perimeter=2*(length+bredth)

#Display area and perimeter

print(f"Area={area}\nPerimeter={perimeter}")
