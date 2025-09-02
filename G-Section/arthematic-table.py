'''
Looping: python 2 loops while and for

syntax: while  condi :
    indented statements
    n
    d
    e
    n
    t
    e
    d statements indent

    for i in range():
    i in range(3)--->i 0 ,1 ,2,
    i in range(1,3)--->i 1 ,2,
    i in range(3,-1,-1)--->i 3, 2, 1, 0
'''

#Printing mathematical table

number=int(input("Enter the no: "))

#printing table
'''
for i in range(1,11):
    print(f"{number} X {i} = {number*i}")
'''
print("\n".join(f"{number} X {i} = {number*i}"for i in range(1,11)))
    

