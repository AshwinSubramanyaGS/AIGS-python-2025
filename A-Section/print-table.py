'''
while condi:
    indented block
    n
    d
    e
    n
    ted block inde
'''

#Print mathematical table using loop

number=int(input("Enter a no: "))

#for logic to print tables

'''
for i in range(1,11):
    print(f"{number} X {i} = {number*i}")
'''
#print("\n".join(f"{number} X {i} = {number*i}"for i in range(1,11)))
i=1
#while loop print table
while i in range(1,11):
    print(f"{number} X {i} = {number*i}")
    i+=1


    
