print("Pleasee Enter he below details:-")
name=input("Enter your name = ")
enroll=input("Enter your  enrollment number = ")
sem=input("Enter your semster = ")

print("\n Select the given below service ")
print( " \n 1.View Details \n 2. Get your Result\n")

choice=int(input("enter your service number :- "))

match choice:
    case 1:
        print(f"\nName= {name} \nEnrollment Number= {enroll} \nSemester = {sem}")
    case 2:
        print("!!!!!!!   Enter Your Marks (In range of 100)  !!!!!!")

        java=int(input("Enter Marks for Java="))
        python=int(input("Enter Marks for Python="))
        javascript=int(input("Enter Marks for Javascript="))

        sum1=java+javascript+python

        avg=(sum1/300)*100

        print(f" Percentage ={int(avg)} %")

        if(avg<=100 and avg>=90):
            print("A grade \n Congratulations !! You have Distiction")
        elif(avg<=90 and avg>=80):
            print("B+ grade \n Congratulations You have First class ")
        elif(avg<=80 and avg>=60):
            print("B grade \n Congratulations You have Second class") 
        elif(avg<=60 and avg>=50):
            print("D garde \nYou have Cleared the exams")
        else:
            print("Failed !!!!\n ")