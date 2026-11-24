
device_status = "active"   
temperature = int(input("Enter the temperature: "))
if device_status == "active":
    if temperature > 30:
        print("Device is active and temperature is high!")

    else:
        print("Device is active and temperature is normal.")