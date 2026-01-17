fruits='mango,kiwi,apple,kiwi'
print("Fruits=",fruits)

print(f"Number of p in fruits={fruits.count('p')}")

#capatalize(),title(),upper(),lower()
print(f"Title of= {fruits.title()}")

vegie="Onion"
print(f"Capitalize of= {vegie.capitalize()}")
print(f"Uppercase={vegie.upper()}")
print(f"Uppercase={vegie.lower()}")

#istitle,islower,isupper
print(f"Is Capitalize ?  {vegie.istitle()}")
print(f"Is Uppercase? {vegie.isupper()}") 
print(f"Is lowercase? {vegie.islower()}")

#find(),rfind() = shows rightmost ,replace()
print(f"Find kiwi in fruits= {fruits} \nFound at ={fruits.find('kiwi')}")
print(f"Find kiwi in fruits= {fruits} \nFound at ={fruits.rfind('kiwi')}")
print(f"Replace mango from peace \n{fruits.replace('mango','peace')}")

#strip()rstrip(),lstrip()

name=' Heer '
print(name)

print(f"Strip of {name} = {name.strip()}\n ")
print(f"Rightstrip of {name} = {name.rstrip()}")
print(f"LeftStrip of {name} = {name.lstrip()}")
