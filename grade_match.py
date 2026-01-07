grade=str(input("Ente your grade="))

match grade:
    case 'A'| 'a':
        print("Excellent")
    case 'B' | 'b':
        print("Very good")
    case 'C'| 'c':
        print("Good")
    case 'D'| 'd':
        print("Failed")
    case _:
        print("Invalid input")