num=0
a=0
while num<5:
    print(f"{a} {a}")
    num+=1

print("\n Pattern 2 \n")

num=1
num1=0
while num<6:
    while num1<10:
        print(f"{num}  {num1}")
        num1+=2
        num+=1

print("\n Pattern 3")
a=1
num=1
while num<6:
    print(f"{a} {a+1} {a+2}")
    num+=1


print("\n\n Pattern 4 \n\n")
num=1
while num<=3:
    print("0 8")
    num+=1
num=1
a=1
b=3
while num<=3: 
    print(f"{a} {b}")
    a+=1
    b-=1
    num+=1

print("\n\n Pattern 5 \n\n")
num=1
a=1
b=5
c=0
while num<6:
    print(f"{c} {a} {b} {c}")
    a+=1
    b-=1
    num+=1

print("\n\n Pattern 5\n")
num=2
while num<=10:
    print(num)
    num+=2 

num=8
while num>0:
    print(num)
    num-=2

print("\n\n Pattern-6\n")
num=0
while num<=13:
    print(num)
    num+=3 

num=9
while num>=0:
    print(num)
    num-=3

print("\n\n Pattern-7\n\n")
num=0
a=0
b=0
c=0
while num<=5:
    print(f"{a}  {b}  {c}  {a}")
    b+=1
    c+=2
    num+=1
num=0
b=4
c=8
while num<5:
    print(f"{a}  {b}  {c}  {a}")
    b-=1
    c-=2
    num+=1

print("\n\n Pattern-8\n")
num=0
a=0
b=0
c=0
while num<6:
    print(f"{a} {b} {c}")
    a+=1
    b+=2
    c+=3
    num+=1
a=4
b=8
c=12
num=0
while num<5:
    print(f"{a} {b} {c}")
    a-=1
    b-=2
    c-=3
    num+=1
print("\n\n Pattern-9\n\n")
a=0
b=0
c=0
d=0
num=0
while num<6:
    print(f"{a} {b} {c} {d}")
    a+=1
    b-=2
    c-=1
    d-=3
    num+=1

print("\n\n Pattern-10\n\n")
num=0
a=0
b=3
while num<4:
    print(f"{a} {a} {a} {b} {a} {a} {a}")
    a+=1
    num+=1
a=2
num=2
while num>=0:
    print(f"{a} {a} {a} {b} {a} {a} {a}")
    a-=1
    num-=1