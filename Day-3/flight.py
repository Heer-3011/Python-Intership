total_seats=int(input("Enter Total seats in plane="))
booked=int(input("Enter seats booked="))

available=total_seats-booked

booking=int(input("Enter number of seats you want to book="))
if available>=booking:
    print("Seats booked")
else:
    print("!!! Already  Booked !!!")