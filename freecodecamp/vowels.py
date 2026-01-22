def to_consonant_case(s):
    s1=""
    for i in s :
        i=i.lower()
        if i== 'a' or i=='i' or i=='u' or i=='e' or i=='o':
            s1+=i.lower()
        elif i=='-':
            s1+=i.replace('-','_')
        else:
            s1+=i.upper()
    return s1

print(to_consonant_case("_~-generic_~-variable_~-name_~-here-~_"))

str1=("heer2")
print(str1.upper())