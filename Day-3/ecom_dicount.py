print("!!!Dicount Caculation!!!!")

bill=int(input("Enter bill amount= "))

if bill>1500 and bill<2000:
    disc=bill*0.10
    print(f"Dicount of {disc}")
    print(f"Amount to be paid={bill-disc}")

elif bill>2000 and bill<3000:
    disc=bill*0.20
    print(f"Dicount of {disc}")
    print(f"Amount to be paid={bill-disc}")
