def grade_system(java,javascript,python):

    sum1=java+javascript+python

    avg=(sum1/300)*100
    
    print(f"sum={sum1}, avg={avg}")

    if(avg<=100 and avg>=90):
        return("A grade")
    elif(avg<=90 and avg>=80):
        return("B+ grade")
    elif(avg<=80 and avg>=70):
        return("B grade")
    elif(avg<=70 and avg>=60):
        return("C garde")
    elif(avg<=60 and avg>=50):
        return("D garde")
    else:
        return("Failed")
    
print("!!!!!!!   Enter Your Marks (In range of 100)  !!!!!!")

java=int(input("Enter Marks for Java="))
python=int(input("Enter Marks for Python="))
javascript=int(input("Enter Marks for Javascript="))

print(grade_system(java,javascript,python))

