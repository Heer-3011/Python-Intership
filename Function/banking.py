def banking(amount,withdrawal):
    if amount>withdrawal:
        return(f"WITHDRAWAL SUCCESSFULL!!!\nRemaining balance={amount-withdrawal}") 
    else:
        return("Insuffiecent Balance")

print("!!!!! Bank withdrawal !!!!!!")

amount=int(input("Enter you bank balance="))
withdrawal=int(input("Enter withdrawal="))
print(banking(amount,withdrawal))   