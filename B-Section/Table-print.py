'''
while condi:
    indented block
    n
    d
    e
    n
    ted block inde
'''
#Program to print tables

number=int(input("Enter a number: "))

#logic to print mul table
'''
i=1
while i<11:
    print(f"{number} X {i} = {number*i}")
    i+=1
'''
'''
for i in range(1,11):#->i=1 to i=11
    print(f"{number} X {i} = {number*i}")
'''
print("\n".join(f"{number} X {i} = {number*i}"for i in range(1,11)))

