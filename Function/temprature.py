def temprature(temp):
    if temp<20:
        return ("Temprature is too low \n Its cold and breeze outside")
    elif temp>20 and temp<30:
        return("Normal temprature \n Perfect weather")
    else:
        return("Temprature is too highh !! \n Its hot outside")
    
temp=int(input("Enter Temprature in degree="))
print(temprature(temp))