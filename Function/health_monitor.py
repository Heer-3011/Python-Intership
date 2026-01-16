def monitor(heart_rate):
    if heart_rate>60 and heart_rate<100:
        return("Normal heart rate , Healthy body")
    else:
        return("Abnormal Heart rate, See a Doctor")

heart_rate=int(input("Enter you heart rate="))
print(monitor(heart_rate))