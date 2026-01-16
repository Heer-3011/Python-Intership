def sum():
    a=10
    b=10
    print(a+b)

sum()

def factorial():
    num=r=int(input("enter number to find factorial: "))
    fact=1
    for i in range(1,num+1,1):
        fact*=i 
    print(f"Factorial of {num} ={fact}")
factorial()

def circle():
    r=int(input("enter radius: "))
    print(f"Area of radius: {3.14*r*r}")

circle()

def simple_intrest():
    p=int(input("Enter Principle="))
    n=int(input("Enter Year="))
    r=int(input("Enter Rate="))
    
    #print(f"Simple intrest={(p*r*n)/100}")
    return((p*r*n)/100)

print(simple_intrest())

def fact_return():
    fact=1
    num=int(input("Enter Nummber="))
    for i in range(1,num+1,1):
        fact*=i
    return fact

print(fact_return())

def info():
    return("Heellloo Heerr!!\n")

print( info())
 
def sum():
    a=10
    b=10
    print(a+b)
    return(info())

print(sum())