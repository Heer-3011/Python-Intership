full_dot = '●'
empty_dot = '○'
def create_character(name,strength, intelligence,charisma):
    if type(name)=='str':
        return 'The character name should be a string.'
    elif name=="":
        return 'The character should have a name.'
    elif len(name)>10:
        return 'The character name is too long' 
    elif " " in name:
         return 'The character name should not contain spaces.' 
    elif type(strength)== "int" and type(intelligence)== "int" and type(charisma) == "int":
        return "All stats should be intergers."

    elif strength<1 and intelligence<1 and charisma<1:
        return "All stats should be no less than 1"
    
    elif strength>5 and intelligence>5 and charisma>5:
        return "All stats should be no more than 4"

    elif strength+intelligence+charisma !=7:
        return "The character should start with 7 points"
    else:
        return f"{name}\n STR  {full_dot*strength}{empty_dot*(10-strength)}\n INT  {full_dot*intelligence}{empty_dot*(10-intelligence)} \n CHA  {full_dot*charisma}{empty_dot*(10-charisma)}"
        #return chr1
print(create_character('ren', 4, 2, 1))

    
