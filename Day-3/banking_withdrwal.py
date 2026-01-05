print("!!!!! Bank withdrawal !!!!!!")

amount=int(input("Enter you bank balance="))
withdrawal=int(input("Enter withdrawal="))

if amount>withdrawal:
    print("WITHDRAWAL SUCCESSFULL!!!")
    print(f"Remaining balance={amount-withdrawal}")
else:
    print("Insuffiecent Balance")