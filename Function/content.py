def age_verfication(age):
    if age>=18:
        return("You are eligible for Viewing this content\nEnjoy binge !!!!") 
    else:
        return("You are not eligible for watching this content\nAccess Denied !!!!") 

age=int(input("Enter your age ="))
print(age_verfication(age))