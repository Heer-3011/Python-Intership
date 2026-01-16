print("!!!Dicount Caculation!!!!")

def ecom_dicount_system(bill):

    if bill>1500 and bill<2000:
        disc=bill*0.10 
        return (f"Dicount of {disc} \n Amount to be paid={bill-disc}")

    elif bill>2000 and bill<3000:
        disc=bill*0.20
        return (f"Dicount of {disc} \n Amount to be paid={bill-disc}")
    elif bill>3000:
        disc=bill*0.30
        return (f"Dicount of {disc} \n Amount to be paid={bill-disc}")
    else:
        return(f"!!Sorry No discount \n Amount to be paid={bill}")

bill=int(input("Enter bill amount= "))
print(ecom_dicount_system(bill))