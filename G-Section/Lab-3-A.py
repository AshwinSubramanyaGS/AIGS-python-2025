#Fibbnocci Series

#Declare limit and take Input
limit=int(input("Enter the limit: "))

f1=0
f2=1
f3=f1+f2

while f1<=limit:
    print(f1,", "if f2<limit else " ",end=' ')
    f3=f1+f2
    f1=f2
    f2=f3
