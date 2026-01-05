print("******* Weather Acitvity Suggestion *******")
print(" 1. Sunny ")
print(" 2. Rainy ")
print(" 3. Cold ")
weather=int(input("Enter the current weather value from list above="))

if weather==1:
    paragraph = """ \nAs it is sunny day, Following are some acitvity suggestion :- \n 
    1.Indoors: DIY spa, movie marathon, baking, indoor yoga, puzzles \n
    2.Outdoors: Hiking, swimming, picnics, biking, visiting botanical gardens"""
    print(paragraph)

elif weather==2:
    paragraph = """ \nAs it is sunny day, Following are some acitvity suggestion :- \n 
    1.Indoors: Bake comfort food, read by a window, build a blanket fort, play games \n
    2.Outdoors:  visit a museum/gallery, explore a cozy cafe, or try rainy day photography. """
    print(paragraph)

elif weather==3:
    paragraph = """ \nAs it is sunny day, Following are some acitvity suggestion :- \n 
    1.Indoors: Host a football party, make hot chocolate, learn to knit, or have a cozy reading day \n
    2.Outdoors:  visit a museum/gallery, explore a cozy cafe, or try day photography. """
    print(paragraph)
else:
    print("Invalid Input")