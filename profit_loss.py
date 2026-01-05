sp=int(input("Enter Selling Price="))
cp=int(input("Enter Cost Price="))

if sp>cp:
    print(f"Profit of {sp-cp}")
elif cp>sp:
    print(f"Loss of {cp-sp}")
else:
    print("No progit no loss")