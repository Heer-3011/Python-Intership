print("Pattern-20\n\n")
for i in range(1,6,1): 
    for j in range(1,6-i,1): 
        print(" ",end=" ")
    for j in range(1,i+1,1):
        print("*",end=" ")
    print("\n") 

print("Pattern-20\n\n")
for i in range(1,6,1):
    for j in range(1,i+1,1):
        print("*",end=" ") 
        if i==5: 
            for i in range(5,0,-1):
                for j in range(1,i+1,1):
                    print("*",end=" ")
                print("\n") 
    print("\n")

print("Pattern-21\n\n")
k=1

for i in range(1,6,1):
    for j in range(1,6-i,1):
        print("",end=" ")
    for j in range(5,6-i,-1):
        print(k,end=" ")
        k+=1
    print("\n")  
