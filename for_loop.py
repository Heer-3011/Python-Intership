for i in range(0,11,1):
    print(i)

print("\n Printing 10 to 1\n")
for i in range(10,-1,-1):
    print(i)

print("\n Printing 1 to 10 and sum of it\n")
sum=0
for i in range(0,11,1):
    print(i)
    sum+=i
print("sum",sum)

print("\n\n Printing table for 5\n")
a=5
for i in range(1,10,1):
    print(f"{a} X {i} = {a*i}")

print("\n\n Table from 1 to 10\n\n")
for i in range(1,10,1):
    print(f"\nTable of {i}\n\n")
    for j in range(1,10,1): 
        print(f"{i} X {j} = {j*i}")