import datetime
x=datetime.datetime.now()
print(x)

#strftime string format time 
#print(f"String formatr time (%A) = {x.strftime("%A")} ")

print(f"strftime(%A)= {x.strftime('%A')}")
print(f"strftime(%a) Short form of day = {x.strftime('%a')}")
print(f"strftime(%c)= {x.strftime('%c')}\n")

print(f"strftime(%M) Shows minute = {x.strftime('%M')}")
print(f"strftime(%H) Show hour = {x.strftime('%H')}")
print(f"strftime(%S) show seconds= {x.strftime('%S')}")

print(f"strftime(%W) show week ={x.strftime('%W')}")  
print(f"strftime(%x) show date={x.strftime('%x')}")
print(f"strftime(%d %m %y)={x.strftime('%d - %m - %Y')}")
print(f"strftime(%d %B %Y %A)={x.strftime('%d  %B  %Y , %A')}")


 