print("\n\n Pattern-11\n\n ")
num=0
a=0
b=1
c=2
d=3
while num<3:
    print(f"{a} {b} {c} {d} {c} {b} {a} ")
    b+=1
    c+=1
    d+=1
    num+=1
a=0
b=2
c=3
d=4
num=2
while num>0:
    print(f"{a} {b} {c} {d} {c} {b} {a} ")
    b-=1
    c-=1
    d-=1
    num-=1

print("\n\n Pattern-12\n\n ")
a=0
b=0
c=0
d=0
e=0
f=0
num=0
while num<3:
    print(f"{a} {b} {c} {d} {e} {f}")
    b+=1
    c+=2
    d+=3
    e+=4
    f+=5
    num+=1
num=0 
while num<4:
    print(f"{a} {b} {c} {d} {e} {f}")
    b-=1
    c-=2
    d-=3
    e-=4
    f-=5
    num+=1

print("\n\n Pattern-13\n\n ")
a=0
b=0
num=0
while num<10:
    print(f"{a} {b} {b} {b} {b} {b}")
    if b==9:
        print(f"{a} {a+1} {a+2} {a+3} {a+4} {a+5}")
    b+=1
    num+=1

print("\n\n Pattern-14\n\n ")
a=0
b=0
num=0
while num<10:
    print(f"{a} {b} {b} {b} {b} {b}")
    if b==9:
        print(f"{a} {a} {a} {a} {a} {a}")
    b+=1
    num+=1

print("\n\n Pattern-15\n\n ")
a=0
b=0
c=0
num=0
while num<4:
    print(f"{a} {b} {c} {a}")
    if b==3 and c==6:
        print(f"{a} {b-1} {c-2} {a}")
        print(f"{a} {b-2} {c-4} {a}")
        print(f"{a} {b-3} {c-6} {a}")
    b+=1
    c+=2
    num+=1

 