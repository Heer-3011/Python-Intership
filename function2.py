def sum(a,b):
    return(a+b)
a=10
b=20
print(f"{a} + {b} = {sum(a,b)}")

def fact(num):
    fact=1 
    for i in range(1,num+1,1):
        fact*=i
    return fact

num=int(input("Enter number for factorial="))
print(f"Factorial of {num}= {fact(num)}")

def simple_intrest(p,n,r): 
    return((p*r*n)/100)

p=int(input("Enter Principle="))
n=int(input("Enter Year="))
r=int(input("Enter Rate="))
print(f"Simple intrest={simple_intrest(p,n,r)}")

def info(name,enrollment,marks):
    print(f"\nName={name} \n Enrollment={enrollment} \n Marks={marks}")

info("Heer",54009,23)


def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci sequence:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b 
    print()

fibonacci(10)
