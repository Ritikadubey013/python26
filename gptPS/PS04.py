a=int(input("enter the price:"))
b=int(input("enter the qty:"))
c=float(input("enter the discount"))

total=a*3

print("total price before discount",total)

dist=(10/100)*total
print("discount",dist)

famt=total-dist
print("final amount",famt)