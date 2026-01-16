def booking_seats(booking,booked=100,total_seats=200):
    available=total_seats-booked
    if available>=booking:
        return("Seats booked")
    else:
        return("!!! Already  Booked !!!")

booking=int(input("Enter number of seats you want to book="))
print(booking_seats(booking))