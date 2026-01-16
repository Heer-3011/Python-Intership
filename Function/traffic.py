def traffic_light(light):
    if light=="red" or light=="Red":
        return("!!!!!!!!! Please Stop !!!!!!!")
    elif light=="green" or light=="Green":
        return("###### You May goo ######")
    elif light=="yellow" or light=="Yellow":
        return("###### Prepare to Stop #####")
    else:
        return("Invalid Input")

light=input("Enter traffic light=")
print(traffic_light(light))
