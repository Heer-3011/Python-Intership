class bank:
    def __init__(self):
        print("\n !!!!! Welcome to XYZ Bank  !!!!")
        print("\n Please enter the details below:- \n")
        self.name=str(input("Enter Name :-"))
        self.account_number=int(input("Enter accouunt number  :-"))
        self.password=int(input("Set passworrd :-"))
        self.bank_balance=int(input("Enter bank balance :-"))

    def login(self):
        print("\n\n Login required \n")
        user=input("Enter user name :-")
        pass1=int(input("Enter Password :-"))

        if user==self.name and pass1==self.password:
            print("\n\n Login Successfull \n\n")
            print("\n Select  any service from given below List")
            print("\n   1.View deatils \n   2.Deposit Money\n  3.Withdraw Money\n\n")
        else:
            print("Login Failed ! Retry again ")

    def service(self):
        service=int(input("Enter the number of service :-"))
        
        match service:
            case 1:
                print(f"\n Here are the details :-\n Name = {self.name} \n Account number= {self.account_number} \n Bank Balance= {self.bank_balance}\n")

            case 2:
                deposit=int(input("\n Enter the amount of money you want to deposit :-"))
                self.bank_balance+=deposit
                print("Deposit Successfull")
                print(f"Current bank balance= {self.bank_balance}")
            case 3:
                withdraw=int(input("\n Enter the amount of money you want to withdraw :-"))
                if withdraw<=self.bank_balance:
                    self.bank_balance-=withdraw
                    print("Withdraw Successfull")
                    print(f"Current bank balance= {self.bank_balance}")
                else:
                    print("Insufficient Balance")

bank1=bank()
bank1.login()
bank1.service()