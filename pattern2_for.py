print("\n\n Pattern-11\n\n")
a=0
b=0
c=0
for i in range(1,5,1):
    print(a,b,c,a)
    b+=1
    c+=2
b=2
c=4
for i in range(1,4,1):
    print(a,b,c,a)
    b-=1
    c-=2

print("\n\n Pattern-12\n\n")
a=0
b=0
c=0
for i in range(0,6,1):
    print(i,a,b,c)
    a-=2
    b-=1
    c-=3

print("\n\n Pattern-13\n\n")
b=3
for i in range(1,4,1):
    print(i,i,i,b,i,i,i)
    if i==3:
        for j in range(2,-1,-1):
            print(j,j,j,b,j,j,j)
    
print("\n\n Pattern-14\n\n")
a=0
for i in range(1,4,1):
    print(a,i,i+1,i+2,i+1,i,a)
for i in range(2,0,-1):
    print(a,i,i+1,i+2,i+1,i,a)

print("\n\n Pattern-14\n\n")
a=0
b=0
c=0
d=0
e=0
f=0
for i in range(1,5,1):
    print(a,b,c,d,e,f)
    b+=1
    c+=2
    d+=3
    e+=4
    f+=5 
a=0
b=2
c=4
d=6
e=8
f=10
for i in range(2,1,-1):
    
    b-=1
    c-=2
    d-=3
    e-=4
    f-=5
    print(a,b,c,d,e,f)

print("\n\n Pattern-15\n\n")

for i in range(0,10,1):
    print(a,i,i,i,i,i)
    if i==9:
        print(a,a+1,a+2,a+3,a+4,a+5)
    
print("\n\n Pattern-16\n\n")

for i in range(0,10,1):
    print(a,i,i,i,i,i)
    if i==9:
        print(a,a,a,a,a,a)