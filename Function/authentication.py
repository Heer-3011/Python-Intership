def login(username,password):
    if username=="Heer" and password=="Heer@123":
        return (" !!!!!! Successfully Logged In !!!!!!")
    elif username=="Heer":
        return ("!!!! Incorect password")
    elif password=="Heer@123":
        return ("!!!! Incorect username")
    else:
        return("!!!!Login failed")

username=(input("Enter Username="))
password=(input("Enter Password="))
print(login("Heer","Heer@123"))