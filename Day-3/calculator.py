print("\n\n!!!!!     Calculator  !!!!!!!!\n\n")
print("Enter values of two numbers:\n")
num1=float(input("Enter The value for first number:-"))
num2=float(input("Enter The value for second number:-"))

print(" \n!!!!! Opeartions !!!!!\n")
print("       1.Addition (+)\n")
print("       2.Substraction (-)\n")
print("       3.Multiplication (*)      \n")
print("       4.Divion (/)\n")
print("       5.Modulo (%)\n")
print("       6.Floor Division (//)\n")
operation=int(input("Select form the above given operations="))

if operation==1:
    print(f"Addtion of {num1} + {num2} = {num1+num2}")

elif operation==2:
    print(f"Substraction of {num1} - {num2} = {num1-num2}")

elif operation==3:
    print(f"Multiplication of {num1} * {num2} = {num1*num2}")

elif operation==4:
    print(f"Divion of {num1} / {num2} = {num1/num2}")

elif operation==5: 
    print(f"Modulo of {num1} % {num2} = {num1%num2}")

elif operation==6:
    print(f"Floor Division of {num1} // {num2} = {num1//num2}")

else:
    print("!!!  Invalid Input  !!!")