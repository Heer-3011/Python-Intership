print("!!!!!!!   Enter Your Marks (In range of 100)  !!!!!!")

java=int(input("Enter Marks for Java="))
python=int(input("Enter Marks for Python="))
javascript=int(input("Enter Marks for Javascript="))

sum1=java+javascript+python

avg=(sum1/300)*100

print(f"sum={sum1}, avg={avg}")

if(avg<=100 and avg>=90):
    print("A grade")
elif(avg<=90 and avg>=80):
    print("B+ grade")
elif(avg<=80 and avg>=70):
    print("B grade")
elif(avg<=70 and avg>=60):
    print("C garde")
elif(avg<=60 and avg>=50):
    print("D garde")
else:
    print("Failed")