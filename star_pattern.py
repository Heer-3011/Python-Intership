print("Reverse triangle 1 to 5\n\n")
for i in range(5,0,-1):
    for j in range(1,i+1,1):
        print(j,end=" ")
    print("\n")

print("Reverse triangle *\n\n")
for i in range(5,0,-1):
    for j in range(1,i+1,1):
        print("*",end=" ")
    print("\n")

print("Reversed triangle increment with 2")
for i in range(0,10,2):
    for j in range(i,-1,-1):
        print(j,end=" ")
    print("\n")

print("Reversed triangle increment with 1")
for i in range(5,0,-1):
    for j in range(5,i+1,-1):
        print(j,end=" ")
    print("\n")

print("Pattern-5\n\n")
k=1
for i in range(1,6,1):
    for j in range(i,k+1,1):
        print(j,end=" ")
    k+=2
    print("\n")

print("Pattern-6\n\n")
k=8
for i in range(0,5,1):
    for j in range(i,k+1,2): 
        print(j,end=" ")
    k-=1
    print("\n")

print("Pattern-7\n\n")
k=1
for i in range(1,5,1):
    for j in range(1,i+1,1):
        print(k,end=" ")
        k+=1
    print("\n")

'''
0 2 
1 3 5 
2 4 6 8 
3 5 7 9 11
'''
print("Pattern-8\n\n")
k=2
for i in range(0,4,1):
    for j in range(i,k+1,2):
        print(j,end=" ")
    k+=3
    print("\n\n")

print("Pattern-9\n\n")
for i in range(1,6,1):
    for j in range(1,6-i,1):
        print("   ",end=" ") 
    for j in range(1,6,1):
        print(i,end=" ")
    print("\n")

print("Pattern-10\n\n")
for i in range(1,6,1):
    for j in range(1,6-i,1):
        print("   ",end=" ") 
    for j in range(1,6,1):
        print(j,end=" ")
    print("\n")
