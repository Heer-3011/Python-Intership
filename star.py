print("\n\n 1 to 5 Box pattern\n\n")
for i in range(1,6,1):
    for j in range(1,6,1):
        print(j,end=" ")
    print(" ")

print("\n\n Left 1 to 5 triangle pattern\n\n")
for i in range(1,6,1):
    for j in range(1,i+1,1):
        print(j,end=" ")
    print(" ")

print("\n\n Left 5 to 1 triangle pattern\n\n")
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print(" ")

print("\n\n Right triangle for 2 multiple\n")
for i in range(0,9,2):
    for j in range(0,i+2,2):
        print(j,end=" ")
    print(" ")

print("\n\n Right triangle for 3 multiple\n")
for i in range(0,13,3):
    for j in range(0,i+3,3):
        print(j,end=" ")
    print(" ")

print("\n\n Pattern-4\n\n")
for i in range(1,6,1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print(" ")

print("\n\n Pattern-5\n\n")
for i in range(0,10,2):
    for j in range(i,-1,-2):
        print(j,end=" ")
    print(" ")

print("\n\n Pattern-6\n\n")
for i in range(0,13,3):
    for j in range(i,-1,-3):
        print(j,end=" ")
    print(" ")
    
print("\n\n Square star pattern")
for i in range(1,6,1):
    for j in range(1,6,1):
        print("*",end=" ")
    print(" ")

print("\n\n Capital A to E pattern")
for i in range(65,70,1):
    for j in range(65,i+1,1):
        print(chr(j),end=" ")
    print(" ")

print("\n\n Small a to e pattern")
for i in range(97,102,1):
    for j in range(97,i+1,1):
        print(chr(j),end=" ")
    print(" ")

print("\n\n  Capital A to E using 1 to 3 loop pattern")
for i in range(0,6,1):
    for j in range(0,i+1,1):
        print(chr(65+j),end=" ")
    print(" ")

print("\n\n a to e using 1 to 3 loop pattern")
for i in range(0,6,1):
    for j in range(0,i+1,1):
        print(chr(97+j),end=" ")
    print(" ")


