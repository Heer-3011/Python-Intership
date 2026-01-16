
print("Pattern-11\n\n")
for i in range(1,6,1):
    for j in range(1,6-i,1):
        print("   ",end=" ") 
    for j in range(1,6,1):
        print(i,end=" ")
    print("\n")
for i in range(5,0,-1):
    for j in range(1,6-i,1):
        print("   ",end=" ") 
    for j in range(1,6,1):
        print(i,end=" ")
    print("\n")

print("\nPattern-12\n\n")
for i in range(1,6,1):
    for j in range(1,i+1,1):
        if i%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print("\n")

print("\nPattern-13\n\n")
for i in range(1,6,1):
    for j in range(1,i+1,1):
        if j%2==0:
            print(j,end=" ")
        else:
            print("0",end=" ")
    print("\n")

print("Pattern-14\n\n")
for i in range(1,6,1):
    for j in range(1,i+1,1):
        if i%2==1 or j%2==1:
            print("1",end=" ") 
        else:
            print("0",end=" ")
    print("\n")

print("Pattern-15\n\n")
for i in range(1,6,1):
    for j in range(1,i+1,1):
        if j%2==0:
            print("0",end=" ") 
        elif j==3:
            print("p",end=" ")
        else:
            print(j,end=" ")
    print("\n")

print("Pattern-16\n\n")
for i in range(1,6,1):
    for j in range(1,6,1):
        if i==5 or j==5 or i==1 or j==1:
            print("1 ",end=" ")
        else:
            print("  ",end=" ")
    print("\n")

print("Pattern-17\n\n")
for i in range(0,9,1):
    for j in range(0,i+1,1):
        print(j,end=" ")
    print("\n")

print("Pattern-18\n\n")
for i in range(1,6,1):
    for j in range(1,6,1):
        if i==1 or i==5 or j==1 or j==5:
            print("1",end=" ")
        elif i==3 and j==3:
            print("3",end=" ")
        else:
            print("2",end=" ")
    print("\n")

print("Pattern-19\n\n")
for i in range(2,11,2):
    for j in range(1,i+1,1):
        if j%2==0:
            print("*",end=" ")
        else:
            print("1",end=" ")
    print("\n")


