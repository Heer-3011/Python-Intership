print("\n !!!!! Welcome to XYZ Bank  !!!!")
print("\n Please enter the details below:- \n")
name=str(input("Enter Name :-"))
account_number=int(input("Enter accouunt number  :-"))
password=int(input("Set passworrd :-"))
bank_balance=int(input("Enter bank balance :-"))

print("\n\n Login required \n")
user=input("Enter user name :-")
pass1=int(input("Enter Password :-"))

if user==name and pass1==password:
    print("\n\n Login Successfull \n\n")
    print("\n Select  any service from given below List")
    print("\n   1.View deatils \n   2.Deposit Money\n  3.Withdraw Money\n\n")

    service=int(input("Enter the number of service :-"))
    
    match service:
        case 1:
            print(f"\n Here are the details :-\n Name = {name} \n Account number= {account_number} \n Bank Balance= {bank_balance}\n")

        case 2:
            deposit=int(input("\n Enter the amount of money you want to deposit :-"))
            bank_balance+=deposit
            print("Deposit Successfull")
            print(f"Current bank balance= {bank_balance}")
        case 3:
            withdraw=int(input("\n Enter the amount of money you want to withdraw :-"))
            if withdraw<=bank_balance:
                bank_balance-=withdraw
                print("Withdraw Successfull")
                print(f"Current bank balance= {bank_balance}")
            else:
                print("Insufficient Balance")

else:
    print("Login Failed ! Retry again ")
