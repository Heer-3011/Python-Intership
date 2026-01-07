num=int(input(("Enter value between 1 to 10 =")))
'''
match num:
    case 5:
        print("Number 5 is given")
    case 6:
        print("Number 6 is given")
    case 7:
        print("Number 7 is given")
    case 8:
        print("Number 8 is given")
    case 9:
        print("Number 9 is given")
    case 10:
        print("Number 10 is given")
    case _:
        print("Out of range!!!")
'''

match num:
    case 1 | 2:
        print("One or Two")
    case 3 | 4:
        print("Three or Four")
    case 5 | 6:
        print("Five or Six")
    case 7 | 8:
        print("Seven or Eight")
    case 9 | 10:
        print("Nine or Ten")