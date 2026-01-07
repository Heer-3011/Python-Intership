num1=int(input("Enter 1 number ="))
num2=int(input("Enter 2 number ="))

operation=str(input("Enter symbol for operator="))

match operation:
    case '+':
        print(f"Addtion of {num1} + {num2} = {num1+num2}")

    case '-':
        print(f"Substraction of {num1} - {num2} = {num1-num2}")

    case '*':
        print(f"Multiplication of {num1} * {num2} = {num1*num2}")

    case '/':
        if num1==0 or num2==0:
            print("cannot be performed")
        else:
            print(f"Divion of {num1} / {num2} = {num1/num2}")

    case '%': 
        print(f" Division of {num1} // {num2} = {num1//num2}")

    case _:
        print("!!!  Invalid Input  !!!")