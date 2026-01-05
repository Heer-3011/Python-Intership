guess=14
while 1 :
    number=int(input("Enter number for guessing="))
    if number==guess:
        print("!!!!!!!! Winner !!!!!!!!!")
        break
    else:
        if number>guess:
            print("Tooo High")
            print("Better Luck next time ")
        else:
            print("Too low")
