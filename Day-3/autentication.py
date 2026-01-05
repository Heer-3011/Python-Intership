print("######### Enter Your Credentials ########")

username=(input("Enter Username="))
password=(input("Enter Password="))

if username=="Heer" and password=="Heer@123":
    print(" !!!!!! Successfully Logged In !!!!!!")
elif username=="Heer":
    print("!!!! Incorect password")
elif password=="Heer@123":
    print("!!!! Incorect username")
else:
    print("!!!!Login failed")